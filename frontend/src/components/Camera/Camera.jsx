import "./Camera.css";

export default function Camera({ videoRef }) {
  return (
    <div className="camera-container">
      <video
        ref={videoRef}
        autoPlay
        playsInline
        muted
        className="camera"
      />
    </div>
  );
}
