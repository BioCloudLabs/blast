import { useState } from "react"

function Web() {
    const [query, set_query] = useState(null)
    const [db, set_db] = useState('')
    const [program, set_program] = useState('')
    const [out, set_out] = useState('')
    const [error, set_error] = useState(false)

    async function handleSubmit(event) {
        event.preventDefault()

        const body = new FormData()

        body.append('query', new File([query], query.name))
        body.append('db', db)
        body.append('program', program)
        body.append('out', out)

        const response = await fetch('http://localhost:5000/blast', {
            method: 'POST',
            body: body
        })

        const data = await response.blob() || response.json()

        if (response.ok) {

        } else {
            console.log(data.message)
        }
    }

    console.log(program)
    console.log(db)
    return (
        <>
            <form onSubmit={handleSubmit}>
                <div>
                    <label htmlFor="query">Enter Query Sequence</label>
                    <input type="file" id="query" onChange={(event) => set_query(event.target.files[0])}/>
                </div>
                <div>
                    <label htmlFor="db">Choose Search Set</label>
                    <select value={db} id="db" onChange={(event) => set_db(event.target.value)}>
                        <option value="pdbaa">PDB protein database</option>
                        <option value="pdbnt">PDB nucleotide database</option>
                    </select>
                </div>
                <div>
                    <label htmlFor="program">Program Selection</label>
                    <select value={program} id="program" onChange={(event) => set_program(event.target.value)}>
                        <option value="blastp">BLASTP</option>
                        <option value="blastN">BLASTN</option>
                        <option value="blastx">BLASTX</option>
                        <option value="tblastn">TBLASTN</option>
                    </select>
                </div>
                <div>
                    <label htmlFor="out">Out</label>
                    <input type="text" id="out" value={out} onChange={(event) => set_out(event.target.value)} />
                </div>
                <button type="submit">BLAST</button>
            </form>
        </>
    )
}

export default Web