import { Button } from '@chakra-ui/react';

import { 
    ArrowBackIcon, 
    ArrowForwardIcon 
} from '@chakra-ui/icons'

export const Links = ({ goToPrevious, goToNext }) => {
    return (
        <>
            <div>
                <Button 
                    colorScheme='blue' 
                    variant='outline' 
                    onClick={ goToPrevious }
                    className='mx-2'
                >
                    <ArrowBackIcon />
                </Button>
                <Button 
                    colorScheme='blue' 
                    variant='outline' 
                    onClick={ goToNext } 
                    className='mx-2'
                >
                    <ArrowForwardIcon />
                </Button>
            </div>
        </>
    )
}