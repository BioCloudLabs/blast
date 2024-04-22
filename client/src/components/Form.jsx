import { Button, useSteps } from '@chakra-ui/react';
import { Steps } from './Steps'
import { Links } from './Links';
import { useState } from 'react';

export const Form = () => {
    const [query, setQuery] = useState(null)
    const [database, setDatabase] = useState('')
    const [program, setProgram] = useState('')

    const { 
        activeStep, 
        goToNext, 
        goToPrevious 
    } = useSteps({ index: 0 })

    return (
        <>
            <Steps activeStep={ activeStep } />
            <div className='flex justify-center items-center flex-col'>
                
                {activeStep === 2 ? (
                    <Button
                        colorScheme='blue' 
                        variant='outline'
                    >
                        BLAST
                    </Button>
                ) : (
                    <Links 
                        goToPrevious={() => goToPrevious()}
                        goToNext={() => goToNext()}
                    />
                )}
            </div>
        </>
    )
}