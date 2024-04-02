import { useEffect, useState } from "react";

export const HelloWorldComponent = () => {
    const [helloWorldMessage, setHelloWorldMessage] = useState<string>('');

    useEffect(() => {
        console.log(window.location.hostname)
        fetch(`http://${window.location.hostname}:5000/`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP Error: ${response.status}`);
            }

            return response.json();
        })
        .then(data => {
            setHelloWorldMessage(data.message);
        })
        .catch(error => {
            console.error(error.message);
        });
    }, []);

    return (
        <div>{ helloWorldMessage }</div>
    );
}
