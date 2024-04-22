import {
    Button, 
    Card, 
    CardBody, 
    Image, 
    Stack, 
    Heading, 
    Text, 
    Divider, 
    CardFooter
} from '@chakra-ui/react';

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
            <Stack direction="row" spacing={4}>
                {programs.map((program, index) => (
                    <Card maxW='sm' key={index}>
                        <CardBody>
                            <Image
                                src={program.src}
                                alt={program.alt}
                                borderRadius='lg'
                            />
                            <Stack mt='6' spacing='3'>
                                <Heading size='md'>{program.heading}</Heading>
                                <Text>
                                    {program.text}
                                </Text>
                            </Stack>
                        </CardBody>
                        <Divider />
                        <CardFooter>
                            <Button variant='solid' colorScheme='blue'>
                                BLAST
                            </Button>
                        </CardFooter>
                    </Card>
                ))}
            </Stack> 
        </>
    )
}