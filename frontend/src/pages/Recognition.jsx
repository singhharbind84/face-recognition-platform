import Camera from "../components/Camera/Camera";
import useCamera from "../hooks/useCamera";

export default function Recognition() {

    const videoRef = useCamera();

    return (

        <div
            style={{
                padding: "30px",
                textAlign: "center"
            }}
        >

            <h1>

                Live Face Recognition

            </h1>

            <Camera videoRef={videoRef} />

        </div>

    );

}
