import { useEffect, useState } from "react";
import api from "../services/api";

export default function useRecognition(videoRef) {

    const [result, setResult] = useState(null);

    const [loading, setLoading] = useState(false);

    useEffect(() => {

        if (!videoRef.current) return;

        const interval = setInterval(async () => {

            if (loading) return;

            if (!videoRef.current) return;

            setLoading(true);

            try {

                const canvas = document.createElement("canvas");

                canvas.width = videoRef.current.videoWidth;

                canvas.height = videoRef.current.videoHeight;

                const ctx = canvas.getContext("2d");

                ctx.drawImage(
                    videoRef.current,
                    0,
                    0,
                    canvas.width,
                    canvas.height
                );

                const blob = await new Promise(resolve =>
                    canvas.toBlob(resolve, "image/jpeg")
                );

                const formData = new FormData();

                formData.append(
                    "image",
                    blob,
                    "frame.jpg"
                );

                const response = await api.post(
                    "/identify",
                    formData
                );

                setResult(response.data);

            }
            catch (err) {

                console.log(err);

            }
            finally {

                setLoading(false);

            }

        },1000);

        return () => clearInterval(interval);

    },[videoRef,loading]);

    return result;

}
