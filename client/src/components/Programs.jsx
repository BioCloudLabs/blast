import {
    Card, 
    CardBody, 
    SimpleGrid,
    Heading, 
    Text, 
    Divider, 
    CardFooter,
    Stack
} from '@chakra-ui/react';

import { Button } from './Button';

const programs = [
    {
        src: '/blastn.jpg',
        alt: 'blastn',
        heading: 'Nucleotide BLAST',
        text: 'BLASTN programs search nucleotide databases using a nucleotide query'
    },
    {
        src: '/blastp.jpg',
        alt: 'blastp',
        heading: 'Protein BLAST',
        text: 'BLASTP programs search protein databases using a protein query'
    },
    {
        src: '/blastx.jpg',
        alt: 'blastx',
        heading: 'blastx',
        text: 'BLASTX search protein databases using a translated nucleotide query'
    },
    {
        src: '/tblastn.jpg',
        alt: 'tblastn',
        heading: 'tblastn',
        text: 'TBLASTN search translated nucleotide databases using a protein query'
    }
]

export const Programs = () => {
    return (
        <>
            <SimpleGrid  columns={{sm: 1, md: 2, lg: 4}} spacing={4} className='p-6 '>
                {programs.map((program, index) => (
                    <div className="relative inline-flex items-center justify-center p-0.5 mb-2 me-2 overflow-hidden text-sm font-medium text-gray-900 rounded-lg bg-gradient-to-br from-green-400 to-blue-600 focus:ring-4 focus:outline-none focus:ring-green-200">
                        <Card maxW='sm' key={index} className='p-2' style={{ boxShadow: '0 25px 50px -12px rgb(0 0 0 / 0.25)'}}>
                            <CardBody>
                                <Stack mt='6' spacing='3'>
                                    <Heading size='md' style={{ fontFamily: 'Geist' }}>{program.heading}</Heading>
                                    <Text>
                                        {program.text}
                                    </Text>
                                </Stack>
                            </CardBody>
                            <Divider />
                            <CardFooter>
                                <Button>
                                    Select
                                </Button>
                            </CardFooter>
                        </Card>
                    </div>
                ))}
            </SimpleGrid> 
        </>
    )
}