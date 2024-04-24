import { useSteps } from '@chakra-ui/react';
import { Steps } from './Steps'
import { Nav } from './Nav';
import { useState } from 'react';
import { Programs } from './Programs'
import { Query } from './Query';
import { Database } from './Database';

export const Form = () => {
    const [query, setQuery] = useState(null)
    const [database, setDatabase] = useState('')
    const [program, setProgram] = useState('')

    const { 
        activeStep, 
        goToNext, 
        goToPrevious 
    } = useSteps({ index: 0 })

    const step = () => {
        switch(activeStep) {
            case 0:
                return <Query />
            case 1:
                return <Database />
            case 2:
                return <Programs />
        }
    }

    return (
        <>
            <Steps activeStep={ activeStep } />
            <div className='flex justify-center items-center'>
                <form>
                    {step()}
                </form>
            </div>
            <Nav 
                activeStep={activeStep}
                goToPrevious={() => goToPrevious()}
                goToNext={() => goToNext()}
            />
        </>
    )
}