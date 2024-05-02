import { useState } from "react"
import { saveAs } from 'file-saver'

function Web() {
    const [query, set_query] = useState(null)
    const [db, set_db] = useState('')
    const [program, set_program] = useState('')
    const [message, set_message] = useState(null)

    const error = {
        1: ' Error in query sequence(s) or BLAST options',
        2: 'Error in BLAST database',
        3: 'Error in BLAST engine',
        4: 'Out of memory',
        5: 'Network error connecting to NCBI to fetch sequence data',
        6: 'Error creating output files',
        255: 'Unknown error'
    }

    function handle_query_change(event) {
        set_query(event.target.files[0])
    }

    function handle_db_change(event) {
        set_db(event.target.value)
    }

    function handle_program_change(event) {
        set_program(event.target.value)
    }

    async function handle_submit(event) {
        event.preventDefault()

        const form_data = new FormData()

        form_data.append('query', new File([query], query.name))
        form_data.append('db', db)
        form_data.append('program', program)

        const response = await fetch(`http://${window.location.hostname}:5000/blast`, {
            method: 'POST',
            body: form_data
        })

        if (response.ok) {
            saveAs(await response.blob())
        } else {
            set_message(error[(await response.json()).message])
        }
    }

    return (
        <>
            <div className="d-flex justify-content-center align-items-center flex-column mt-5 text-center fw-lighter">
                <div className="border-black border p-5 mx-4 mb-5">
                    <div className="fs-1 mb-5">Basic Local Alignment Search Tool</div>
                    <form onSubmit={handle_submit}>
                        <div className="mb-4">
                            <label htmlFor="query" className="mb-3 opacity-75">Enter Query Sequence</label>
                            <input type="file" id="query" className="form-control rounded-0 fw-lighter border-black" onChange={handle_query_change} />
                        </div>
                        <div className="mb-4">
                            <label htmlFor="db" className="mb-3 opacity-75">Choose Search Set</label>
                            <select value={db} id="db" className="form-select rounded-0 text-center fw-lighter border-black" onChange={handle_db_change}>
                                <option value="pdbaa">Protein Data Bank proteins</option>
                                <option value="pdbnt">PDB nucleotide database</option>
                            </select>
                        </div>
                        <div className="mb-5">
                            <label htmlFor="program" className="mb-3 opacity-75">Program Selection</label>
                            <select value={program} id="program" className="form-select rounded-0 text-center fw-lighter border-black" onChange={handle_program_change}>
                                <option value="blastp">Search protein databases using a protein query</option>
                                <option value="blastN">Search nucleotide databases using a nucleotide query</option>
                                <option value="blastx">Search protein databases using a translated nucleotide query</option>
                                <option value="tblastn">Search translated nucleotide databases using a protein query</option>
                            </select>
                        </div>
                        <button type="submit" className="btn btn-outline-primary fw-lighter rounded-0">Submit</button>
                    </form>
                </div>
                {message && (
                    <div className="alert alert-danger rounded-0 mb-5">{ message }</div>
                )}
            </div>
        </>
    )
}

export default Web