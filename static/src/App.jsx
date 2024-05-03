import { Formik, Field, Form, ErrorMessage } from 'formik'
import { saveAs } from 'file-saver'
import { useState } from 'react'

function App() {
    const [error, setError] = useState(false)
    const [loading, setLoading] = useState(false)

    const initialValues = { 
        query: undefined, 
        db: '', 
        program: '', 
        outfmt: undefined
    }

    const validate = values => {
        const errors = {}

        const {query, db, program, outfmt} = values

        if (!query) {
            errors.query = 'Query is required'
        }

        if (!db) {
            errors.db = 'Database is required'
        }

        if (!program) {
            errors.program = 'Program is required'
        }

        if (!outfmt) {
            errors.outfmt = 'Output format is required'
        }

        return errors
    }

    const onSubmit = (values, actions) => {
        const { query, db, program, outfmt } = values

        setLoading(true)
        setError(false)

        const formData = new FormData()

        formData.append('query', new File([query], query.name))
        formData.append('db', db)
        formData.append('program', program)
        formData.append('outfmt', outfmt)

        fetch(`https://${window.location.hostname}/blast`, {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                throw new Error()
            }
            
            return response.blob()
        })
        .then(data => {
            saveAs(data)
        })
        .catch(error => {
            setError(true)
        })
        .finally(() => {
            setLoading(false)
            actions.setSubmitting(false)
        })
    }
    return (
        <>
            <Formik initialValues={initialValues} validate={validate} onSubmit={onSubmit}>
                {({ isSubmitting }) => (
                    <div className='d-flex justify-content-center align-items-center text-center fw-lighter vh-100 flex-column bg-dark text-white'>
                        <div className='border p-5 mx-5 rounded'>
                            <div className='fs-2 mb-5'>Basic Local Alignment Search Tool</div>
                            <Form>
                                <Field id="query" name="query" type="file" className="form-control fw-lighter mb-1" />
                                <ErrorMessage name='query' component='div' className='text-danger' />
                                <Field as="select" id="db" name="db" className="form-select fw-lighter text-center mt-3 mb-1">
                                    <option>db</option>
                                    <option value="env_nt">env_nt</option>
                                    <option value="env_nr">env_nr</option>
                                </Field>
                                <ErrorMessage name='db' component='div' className='text-danger' />
                                <Field as="select" id="program" name="program" className="form-select fw-lighter text-center mt-3 mb-1">
                                    <option>program</option>
                                    <option value="blastn">blastn</option>
                                    <option value="blastp">blastp</option>
                                    <option value="tblastn">tblastn</option>
                                    <option value="blastx">blastx</option>
                                    <option value="tblastx">tblastx</option>
                                </Field>
                                <ErrorMessage name='program' component='div' className='text-danger' />
                                <Field as="select" id="outfmt" name="outfmt" className="form-select fw-lighter text-center mt-3 mb-1">
                                    <option>outfmt</option>
                                    <option value={0}>pairwise</option>
                                    <option value={1}>query-anchored showing identities</option>
                                    <option value={2}>query-anchored no identities</option>
                                    <option value={3}>flat query-anchored, show identities</option>
                                    <option value={4}>flat query-anchored, no identities</option>
                                    <option value={5}>XML Blast output</option>
                                    <option value={6}>tabular</option>
                                    <option value={7}>tabular with comment lines</option>
                                    <option value={8}>Text ASN.1</option>
                                    <option value={9}>Binary ASN.1</option>
                                    <option value={10}>Comma-separated values</option>
                                    <option value={11}>BLAST archive format (ASN.1)</option>
                                    <option value={12}>Seqalign (JSON)</option>
                                    <option value={13}>Multiple-file BLAST JSON</option>
                                    <option value={14}>Multiple-file BLAST XML2</option>
                                    <option value={15}>Single-file BLAST JSON</option>
                                    <option value={16}>Single-file BLAST XML2</option>
                                    <option value={17}>Sequence Alignment/Map (SAM)</option>
                                    <option value={18}>Organism Report</option>
                                </Field>
                                <ErrorMessage name='outfmt' component='div' className='text-danger' />
                                <button type="submit" disabled={isSubmitting} className='btn btn-outline-primary fw-lighter mt-3'>Submit</button>
                            </Form>
                            {loading && (
                                <div class="spinner-border mt-5" role="status">
                                    <span class="visually-hidden">Loading...</span>
                                </div>
                            )}
                            {error && (
                                <div className='alert alert-danger mt-5'>Error creating output file</div>
                            )}
                        </div>
                    </div>
                )}
            </Formik>
        </>
    )
}

export default App
