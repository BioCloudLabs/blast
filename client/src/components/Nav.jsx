import { Button } from "./Button"

export const Nav = ({ activeStep, goToPrevious, goToNext, handleClick }) => {
    const BUTTONS = [
        {
            active: activeStep > 0,
            onClick: goToPrevious,
            content: 'Previous'
        },
        {
            active: activeStep < 3,
            onClick: goToNext,
            content: 'Next'
        },
        {
            active: activeStep === 3,
            content: 'Submit',
            onClick: handleClick
        }
    ]

    return (
        <>
            <div className="mt-12">
                {BUTTONS.map((button, index) => (
                    button.active && (
                        <Button key={index} handler={button.onClick}>
                            { button.content }
                        </Button>
                    )
                ))}
            </div>
        </>
    )
}