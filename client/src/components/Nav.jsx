import { Button } from "./Button"

export const Nav = ({ activeStep, goToPrevious, goToNext }) => {
    return (
        <>
            <div class="fixed bottom-12 w-full text-center">
                {activeStep > 0 && (
                    <Button onClick={goToPrevious}>
                        Previous
                    </Button>
                )}
                {activeStep < 2 && (
                    <Button onClick={goToNext}>
                        Next
                    </Button>
                )}
            </div>
        </>
    )
}