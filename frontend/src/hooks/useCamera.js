import { useEffect, useRef } from "react";

export default function useCamera() {

    const videoRef = useRef(null);

    useEffect(() => {

        async function startCamera() {

            const stream = await navigator.mediaDevices.getUserMedia({

                video: true

            });

            videoRef.current.srcObject = stream;

        }

        startCamera();

    }, []);

    return videoRef;

}
