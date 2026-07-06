import Camera from "../components/Camera/Camera";
import RecognitionCard from "../components/Recognition/RecognitionCard";

import useCamera from "../hooks/useCamera";
import useRecognition from "../hooks/useRecognition";

import "../styles/Recognition.css";

export default function Recognition(){

    const videoRef=useCamera();

    const result=useRecognition(videoRef);

    return(

        <div className="page">

            <h1 className="page-title">

                Live Face Recognition

            </h1>

            <div className="layout">

                <div className="camera-section">

                    <Camera

                        videoRef={videoRef}

                    />

                </div>

                <div className="result-section">

                    <RecognitionCard

                        result={result}

                    />

                </div>

            </div>

        </div>

    )

}
