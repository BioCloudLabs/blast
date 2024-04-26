import { useSteps } from '@chakra-ui/react';
import { Steps } from './Steps'
import { Nav } from './Nav';
import { useState } from 'react';
import { Cards } from './Cards'
import { Input } from './Input';
import { Select } from './Select';
import { Button } from './Button';

export const Form = () => {
    const [querySequence, setQuerySequence] = useState(null)
    const [searchSet, setSearchSet] = useState('')
    const [program, setProgram] = useState('')

    const { activeStep, goToNext, goToPrevious } = useSteps({ index: 0 })

    const steps = () => {
        switch(activeStep) {
            case 0:
                return <Input 
                    value={querySequence}
                    setValue={setQuerySequence}  
                />
            case 1:
                return <Select 
                    value={searchSet}
                    setValue={setSearchSet}
                />
            case 2:
                return <Cards 
                    value={program}
                    setValue={setProgram}
                />
        }
    }

    const handleSubmit = (event) => {
        event.preventDefault()

        if (querySequence && searchSet && program) {
            const formData = new FormData()

            formData.append('query', new Blob([querySequence], {type: querySequence.type}))
            formData.append('database', searchSet)
            formData.append('program', program)
            
            console.log('enviado')

            fetch('http://localhost:5000/blast', {
                method: 'POST',
                body: formData
            })
                .then(response => response.json())
                .then(data => console.log(data))
        }
    }

    return (
        <>
            <Steps activeStep={ activeStep } />
            <div className='flex justify-center items-center flex-col'>
                <form>
                    {steps()}
                </form>
                <Nav activeStep={activeStep} goToPrevious={() => goToPrevious()} goToNext={() => goToNext()} handleClick={handleSubmit} />
            </div>
        </>
    )
}