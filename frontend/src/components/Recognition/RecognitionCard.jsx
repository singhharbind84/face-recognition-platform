import "./RecognitionCard.css";

export default function RecognitionCard({ result }) {

    if (!result) {

        return (

            <div className="card">

                <div className="status">

                    Waiting for recognition...

                </div>

            </div>

        );

    }

    if (!result.match) {

        return (

            <div className="card">

                <div
                    className="status"
                    style={{
                        background:"#dc3545"
                    }}
                >

                    Unknown Person

                </div>

            </div>

        );

    }

    return (

        <div className="card">

            <div className="status">

                Recognized

            </div>

            <img

                src={`http://192.168.75.168:8000/${result.person.image}`}

                alt="Registered"

            />

            <h2>

                {result.person.name}

            </h2>

            <p>

                Confidence :

                {(result.similarity*100).toFixed(2)} %

            </p>

            <p>

                Recognition Time :

                {new Date().toLocaleTimeString()}

            </p>

            <p>

                Status :

                Active

            </p>

        </div>

    );

}
