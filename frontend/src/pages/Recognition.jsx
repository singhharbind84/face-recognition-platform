import { useEffect, useRef, useState } from "react";
import Layout from "../components/Layout";
import api from "../services/api";

export default function Recognition() {

    const videoRef = useRef(null);
    const canvasRef = useRef(null);

    const [capturedImage, setCapturedImage] = useState(null);
    const [result, setResult] = useState(null);
    const [status, setStatus] = useState("Starting Camera...");

    useEffect(() => {

        startCamera();

        return () => stopCamera();

    }, []);

    const startCamera = async () => {

        try {

            const stream = await navigator.mediaDevices.getUserMedia({

                video: true,
                audio: false

            });

            videoRef.current.srcObject = stream;

            setStatus("Camera Ready");

        } catch (err) {

            console.error(err);

            setStatus("Cannot access camera");

        }

    };

    const stopCamera = () => {

        if(videoRef.current?.srcObject){

            videoRef.current.srcObject.getTracks().forEach(track=>track.stop());

        }

    };

    const capture = async () => {

        const canvas = canvasRef.current;

        const video = videoRef.current;

        canvas.width = video.videoWidth;

        canvas.height = video.videoHeight;

        const ctx = canvas.getContext("2d");

        ctx.drawImage(video,0,0);

        const imageData = canvas.toDataURL("image/jpeg");

        setCapturedImage(imageData);

        //---------------------------------------
        // Convert Base64 -> Blob
        //---------------------------------------

        const blob = await (await fetch(imageData)).blob();

        const formData = new FormData();

        formData.append("image",blob,"capture.jpg");

        try{

            const response = await api.post(

                "/identify",

                formData,

                {

                    headers:{

                        "Content-Type":"multipart/form-data"

                    }

                }

            );

            setResult(response.data);

        }

        catch(err){

            console.error(err);

        }

    };

    return(

        <Layout>

            <h1>Live Recognition</h1>

            <h3>{status}</h3>

            <video

                ref={videoRef}

                autoPlay

                playsInline

                width="500"

                style={{

                    border:"2px solid black"

                }}

            />

            <br/><br/>

            <button onClick={capture}>

                Capture

            </button>

            <canvas

                ref={canvasRef}

                style={{display:"none"}}

            />

            <br/><br/>

            {

                capturedImage &&

                <>

                    <h2>Captured Image</h2>

                    <img

                        src={capturedImage}

                        width="250"

                    />

                </>

            }

            {

                result &&

                <>

                    <hr/>

                    <h2>Recognition Result</h2>

                    <p>

                        Match :

                        {result.match ? " YES" : " NO"}

                    </p>

                    <p>

                        Similarity :

                        {result.similarity}

                    </p>

                    {

                        result.person &&

                        <>

                            <h3>

                                {result.person.name}

                            </h3>

                            <img

                                src={`http://192.168.75.168:8000/${result.person.image}`}

                                width="250"

                            />

                        </>

                    }

                </>

            }

        </Layout>

    );

}
