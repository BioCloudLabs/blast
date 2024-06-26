import { Formik, Field, Form, ErrorMessage } from 'formik';  // Importing Formik components for form handling
import { useState } from 'react';  // Importing useState hook for managing component state
import { genomes } from './genomes';  // Importing genomes data

// Main component
function App() {
    // State variables
    const [error, setError] = useState(false);
    const [loading, setLoading] = useState(false);
    const [drosophila, setDrosophila] = useState('');
    const [message, setMessage] = useState('');
    const [file, setFile] = useState(null);

    // Handle file input change
    const handleFileChange = (event) => {
        setFile(event.target.files[0]);
    };

    // Render the database select options based on selected drosophila
    const databaseSelect = () => {
        if (drosophila) {
            return (
                <>
                    <Field as="select" id="db" name="db" className="form-select fw-lighter text-center mt-3 mb-1">
                        <option>Select Drosophila's FASTA</option>
                        {Object.entries(genomes).map(([key, value]) => {
                            if (key === drosophila) {
                                return value.map((fasta, index) => (
                                    <option value={fasta} key={index}>{fasta}</option>
                                ));
                            }
                            return null;
                        })}
                    </Field>
                </>
            );
        }
    };
    
    // Initial form values
    const initialValues = { 
        db: '', 
        out: ''
    };

    // Form validation function
    const validate = values => {
        const errors = {};
        const outRegex = /^(.*\.html|[^.]+)$/;
        const { db, out } = values;

        if (!file) {
            errors.query = 'Query is required';
        }

        if (!db) {
            errors.db = 'Database is required';
        }

        if (!out) {
            errors.out = 'Output name is required';
        } else if (!outRegex.test(out)) {
            errors.out = 'Output name must end with .html or have no extension';
        }

        return errors;
    };

    // Form submission handler
    const onSubmit = (values, actions) => {
        const { db, out } = values;

        setLoading(true);
        setError(false);

        const formData = new FormData();
        formData.append('query', file);
        formData.append('db', db);
        formData.append('out', out);

        fetch(`https://${window.location.hostname}/blast`, {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                return response.json().then(errorResponse => {
                    throw new Error(errorResponse.message);
                });
            }
            
            return response.blob();
        })
        .then(data => {
            window.open(`https://${window.location.hostname}/results/${out}`, '_blank');
        })
        .catch(error => {
            setError(true);
            setMessage(error.message);
        })
        .finally(() => {
            setLoading(false);
            actions.setSubmitting(false);
        });
    };

    return (
        <>
            <Formik initialValues={initialValues} validate={validate} onSubmit={onSubmit}>
                {({ isSubmitting }) => (
                    <div className='d-flex justify-content-center align-items-center text-center fw-lighter vh-100 flex-column bg-dark text-white'>
                        <div className='border p-5 mx-5 rounded'>
                            <div className='fs-2 mb-5'>Basic Local Alignment Search Tool</div>
                            <Form>
                                <input id="query" name="query" type="file" className="form-control fw-lighter mb-1" onChange={handleFileChange} />
                                <ErrorMessage name='query' component='div' className='text-danger' />
                                <Field as="select" value={drosophila} className="form-select fw-lighter text-center mt-3 mb-1" onChange={(event) => setDrosophila(event.target.value)}>
                                    <option value=''>Select Drosophila's Database</option>
                                    {Object.keys(genomes).map((genome, index) => (
                                        <option value={genome} key={index}>{genome}</option>
                                    ))}
                                </Field>
                                {databaseSelect()}
                                <ErrorMessage name='db' component='div' className='text-danger' />
                                <Field id="out" name="out" type="text" placeholder="Select BLAST's output name" className="form-control fw-lighter text-center mt-3 mb-1" />
                                <ErrorMessage name='out' component='div' className='text-danger' />
                                <button type="submit" disabled={isSubmitting} className='btn btn-outline-primary fw-lighter mt-3'>Submit</button>
                            </Form>
                            {loading && (
                                <div className="spinner-border mt-5" role="status">
                                    <span className="visually-hidden">Loading...</span>
                                </div>
                            )}
                            {error && (
                                <div className='alert alert-danger mt-5'>{message}</div>
                            )}
                        </div>
                        <a href={`https://${window.location.hostname}/results`} className='link-light link-offset-2 link-underline-opacity-25 link-underline-opacity-100-hover mt-3'>Results</a>
                    </div>
                )}
            </Formik>
        </>
    );
}

export default App;
