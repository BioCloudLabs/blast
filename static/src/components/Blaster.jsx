import blasterjs from 'biojs-vis-blasterjs'
import { useEffect } from 'react'

function Blaster() {
    useEffect(() => {
        new blasterjs({
            input: "blastinput",
            multipleAlignments: "blast-multiple-alignments",
            alignmentsTable: "blast-alignments-table",
            singleAlignment: "blast-single-alignment"
        })
    }, [])
    return (
        <>
            <div className='d-flex justify-content-center align-items-center fw-lighter text-center flex-column mx-5'>
                <div className='mb-5'>
                    <label htmlFor="blastinput" className="mb-3 opacity-75">Enter Query Output</label>
                    <input type="file" id="blastinput" className='form-control rounded-0 fw-lighter border-black'/>
                </div>
                <div id="blast-multiple-alignments" className='mb-5'></div>
                <div id="blast-alignments-table" className=""></div>
                <div id="blast-single-alignment"></div>
            </div>
        </>
    )
}

export default Blaster