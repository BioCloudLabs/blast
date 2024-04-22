import {
    Stepper,
    Step, 
    StepIndicator, 
    StepStatus, 
    StepIcon, 
    StepNumber, 
    Box, 
    StepTitle, 
    StepSeparator
} from '@chakra-ui/react'

import {
    FaDna, 
    FaDatabase, 
    FaTerminal, 
    FaTimesCircle, 
    FaCheck
} from 'react-icons/fa'

const steps = [
    {
        title: 'Enter Query Sequence', 
        as: FaDna,
    },
    {
        title: 'Choose Search Set', 
        as: FaDatabase,
    },
    {
        title: 'Program Selection', 
        as: FaTerminal,
    },
  ]

export const Steps = ({ activeStep }) => {
    return (
        <>
            <div className='container mx-auto'>
                <Stepper index={activeStep}>
                    {steps.map((step, index) => (
                        <Step key={index}>
                            <StepIndicator>
                                <StepStatus
                                    complete={<StepIcon as={step.as}/>}
                                    incomplete={<StepNumber as={FaTimesCircle}/>}
                                    active={<StepNumber as={FaCheck}/>} 
                                />
                            </StepIndicator>
                            <Box>
                                <StepTitle>{ step.title }</StepTitle>
                            </Box>
                            <StepSeparator />
                        </Step>
                    ))}
                </Stepper>
            </div>
        </>
    )
}