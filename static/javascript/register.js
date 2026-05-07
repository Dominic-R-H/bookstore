function RegisterForm() {

    // Form 
    const [name, setName] = React.useState("");
    const [phone, setPhone] = React.useState("");
    const [email, setEmail] = React.useState("");
    const [password, setPassword] = React.useState("");

    // Errors
    const [nameError, setNameError] = React.useState("");
    const [phoneError, setPhoneError] = React.useState("");
    const [emailError, setEmailError] = React.useState("");
    const [passwordError, setPasswordError] = React.useState("");

    const handleChangeName = (e) => {
        const value = e.target.value;
        setName(value);

        // validate
        let error = "";
        if (!/^[A-Za-z ]*$/.test(value)) {
            error = "Name should contain only letters";
        }
        setNameError(error);
    }

    const handleChangePhone = (e) => {
        const value = e.target.value;
        setPhone(value);

        // validate
        let error = "";
        if (!/^[0-9]*$/.test(value)) {
            error = "Phone should contain only numbers";
        } else if (value.length > 0 && value.length !== 10) {
            error = "Phone must be exactly 10 digits";
        }
        setPhoneError(error);
    }

    const handleChangeEmail = (e) => {
        const value = e.target.value;
        setEmail(value);

        // validate
        let error = "";
        if (value && !/^\S+@\S+\.\S+$/.test(value)) {
            error = "Invalid email format";
        }
        setEmailError(error);
    }

    const handleChangePassword = (e) => {
        const value = e.target.value;
        setPassword(value);

        // validate
        let error = "";
        if (value.length > 0 && value.length < 8) {
            error = "Password must be at least 8 characters";
        }
        setPasswordError(error);
    };


    const csrfToken = document.getElementById("csrf_token").value;
    const registrationError = document.getElementById("registration_error").value;


    return (
        <section className="register">

            <div className="register__container">

                <p class="register__error">
                    {registrationError}
                </p>


                <div className="register__form">

                    <h3 className="register__title">Customer Registration</h3>

                    <form method="POST" action="/register">

                        <input type="hidden" name="csrf_token" value={csrfToken} />

                        <div className="register__group">
                            <label className="register__label">Name</label>
                            <input
                                type="text"
                                name="name"
                                className="register__input"
                                value={name}
                                onChange={handleChangeName}
                                required
                            />
                            {nameError && <p className="register__inputerror">{nameError}</p>}
                        </div>

                        <div className="register__group">
                            <label className="register__label">Phone</label>
                            <input
                                type="text"
                                name="phone"
                                className="register__input"
                                value={phone}
                                onChange={handleChangePhone}
                                required
                            />
                            {phoneError && <p className="register__inputerror">{phoneError}</p>}
                        </div>

                        <div className="register__group">
                            <label className="register__label">Email</label>
                            <input
                                type="email"
                                name="email"
                                className="register__input"
                                value={email}
                                onChange={handleChangeEmail}
                                required
                            />
                            {emailError && <p className="register__inputerror">{emailError}</p>}
                        </div>

                        <div className="register__group register__group--last">
                            <label className="register__label">Password</label>
                            <input
                                type="password"
                                name="password"
                                className="register__input"
                                value={password}
                                onChange={handleChangePassword}
                                required
                            />
                            {passwordError && <p className="register__inputerror">{passwordError}</p>}
                        </div>

                        <button
                            type="submit"
                            className="register__button"
                        >
                            Register
                        </button>

                    </form>

                    <p className="register__footer">
                        Already have an account?
                        <a href="/login" className="register__link">Login</a>
                    </p>

                </div>

            </div>

        </section>
    );
}

ReactDOM.createRoot(document.getElementById("react-register")).render(<RegisterForm />);

