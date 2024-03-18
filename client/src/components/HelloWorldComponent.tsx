import { useEffect, useState } from "react";

export const HelloWorldComponent = () => {
    const [helloWorldMessage, setHelloWorldMessage] = useState<string>('');

    useEffect(() => {
        fetch('http://localhost:5000/')
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
    });

    return (
        <div>{ helloWorldMessage }</div>
    );
}