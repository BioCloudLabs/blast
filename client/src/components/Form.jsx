import { Stepper, useSteps, Step, StepIndicator, StepStatus, StepIcon, StepNumber, Box, StepTitle, StepSeparator, Button } from '@chakra-ui/react';
import { FaDna, FaDatabase, FaCog, FaClock, FaCheck } from 'react-icons/fa';
import { ArrowLeftIcon, ArrowRightIcon } from '@chakra-ui/icons'

const steps = [
    {
        title: 'Enter Query Sequence', 
        icon: FaDna
    },
    {
        title: 'Choose Search Set', 
        icon: FaDatabase
    },
    {
        title: 'Program Selection', 
        icon: FaCog
    },
  ]

export const Form = () => {
    const { activeStep, goToNext, goToPrevious } = useSteps({
        initialStep: 0,
        loop: false
    })

    return (
        <>
            <div className='container mx-auto'>
                <Stepper index={activeStep}>
                    {steps.map((step, index) => (
                        <Step key={index}>
                            <StepIndicator>
                                <StepStatus
                                    complete={<StepIcon as={step.icon}/>}
                                    incomplete={<StepNumber as={FaClock}/>}
                                    active={<StepNumber as={FaCheck}/>} 
                                />
                            </StepIndicator>
                            <Box>
                                <StepTitle>{step.title}</StepTitle>
                                {step.form}
                            </Box>
                            <StepSeparator />
                        </Step>
                    ))}
                </Stepper>
                <Button leftIcon={<ArrowLeftIcon />} colorScheme='blue' variant='outline' onClick={goToPrevious()}>
                    Previous
                </Button>
                <Button rightIcon={<ArrowRightIcon />} colorScheme='blue' variant='outline' onClick={goToNext()}>
                    Next
                </Button>
            </div>
        </>
    )
}