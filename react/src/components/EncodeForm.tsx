import React, { useState } from "react";

interface Data {
    errors: string|null
    value: {
        firstname: string
        lastname: string
        id: string
    }|null
}

const EncodeForm: React.FC = ():JSX.Element => {
    const [enteredEncodedString, setEncodedString] = useState<string>("");
    const [fetchData, setFetchData] = useState<Data>({ errors: null, value: null });

    const encodedStringHandler = (event: React.ChangeEvent<HTMLInputElement>):void => {
        setEncodedString(event.target.value);
    };

    const makeRequest = (encodedString:string):void => {
        const apiUrl:string = 'http://127.0.0.1/api/'
        fetch(apiUrl, {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({"data": encodedString})
        })
        .then((response:Response) => response.json())
        .then((data:string) => {
            setFetchData(JSON.parse(data))
        }).catch(error => console.log(error))
    };

    const submitHandler = (event:React.SyntheticEvent):void => {
        event.preventDefault();
        makeRequest(enteredEncodedString)
        setEncodedString('');
    };

    let responseData:JSX.Element;
    if (fetchData.errors) {
        responseData = <p className="text-danger error-input">{fetchData.errors}</p>
    }
    else if (fetchData.value) {
        responseData = <div>
            <p className="error-input"><strong>First Name: </strong> {fetchData.value.firstname}</p>
            <p className="error-input"><strong>Last Name: </strong>{fetchData.value.lastname}</p>
            <p className="error-input"><strong>ID: </strong>{fetchData.value.id}</p>
        </div>
    }
    else{
        responseData = <div></div>
    }

    return (
        <form onSubmit={submitHandler} method="POST">
            <div className="row mb-3">
                <label htmlFor="encoded_string" className="col-sm-2 col-form-label label-encode">Ecoded Input:</label>
                <div className="col-sm-10 input-encode">
                    <input type="text" name="encoded_string" value={enteredEncodedString} onChange={encodedStringHandler} className="form-control" maxLength={20} required id="encoded_string" />
                </div>
                {responseData}
            </div>
            <button type="submit" className="btn btn-primary">Submit</button>
        </form>
    );
}

export default EncodeForm;
