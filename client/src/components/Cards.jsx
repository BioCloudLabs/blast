import { Card, CardBody, SimpleGrid, Heading, Text, Divider, CardFooter, Stack } from '@chakra-ui/react';
import { Button } from './Button';

const programs = [
    {
        name: 'blastn',
        heading: 'Nucleotide BLAST',
        text: 'BLASTN programs search nucleotide databases using a nucleotide query'
    },
    {
        name: 'blastp',
        heading: 'Protein BLAST',
        text: 'BLASTP programs search protein databases using a protein query'
    },
    {
        name: 'blastx',
        heading: 'blastx',
        text: 'BLASTX search protein databases using a translated nucleotide query'
    },
    {
        name: 'tblastn',
        heading: 'tblastn',
        text: 'TBLASTN search translated nucleotide databases using a protein query'
    }
]

export const Cards = ({ value, setValue }) => {

    const handleClick = (event, name) => {
        event.preventDefault()

        setValue(name)
    }

    return (
        <>
            <SimpleGrid  columns={{sm: 1, md: 2, lg: 2}} spacing={8} className='mx-4 mb-12'>
                {programs.map((program, index) => (
                    <div className="p-0.5 rounded-lg bg-gradient-to-br from-green-400 to-blue-600" key={index}>
                        <Card maxW='sm'>
                            <CardBody>
                                <Stack>
                                    <Heading size='lg' style={{ fontFamily: 'Geist' }}>
                                        {program.heading}
                                    </Heading>
                                    <Text>
                                        {program.text}
                                    </Text>
                                </Stack>
                            </CardBody>
                            <Divider />
                            <CardFooter>
                                <Button handler={(event) => handleClick(event, program.name)}>
                                    {value === program.name ? 'Selected' : 'Select'}
                                </Button>
                            </CardFooter>
                        </Card>
                    </div>
                ))}
            </SimpleGrid> 
            <div className='text-center'>
                {!value && 'No Program Selected'}
            </div>
        </>
    )
}
