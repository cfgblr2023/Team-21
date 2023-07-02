import React, { useState } from "react";
import { AiOutlineEye, AiOutlineEyeInvisible } from "react-icons/ai";
import { toast } from "react-hot-toast";
import { Router, useNavigate } from "react-router-dom";

const SignupForm = ({ setIsLoggedIn }) => {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    name: "",
    address: "",
    email: "",
    password: "",
    confirmPassword: "",
    qualification: "",
    languages: [],
    gender: "",
    education: "",
    phone: "",
    availability: "",
    dob: "",
    project_id: "1",
  });
  const [formDataM, setFormDataM] = useState({
    name: "",
    email: "",
    password: "",
    confirmPassword: "",
    languages: [],
    education: "",
    phone: "",
    dob: "",
    address: "",
    project_id: "1",
  });

  function checkboxChangeHandler(event) {
    const { value, checked } = event.target;

    // Update the form data state or perform any desired actions based on the checkbox change
    if (checked) {
      // Add the selected language to the languages array
      formData.languages.push(value);
    } else {
      // Remove the deselected language from the languages array
      const index = formData.languages.indexOf(value);
      if (index > -1) {
        formData.languages.splice(index, 1);
      }
    }

    // You can access the updated form data with formData.languages
    console.log(formData.languages);
  }
  function checkboxChangeHandlerM(event) {
    const { value, checked } = event.target;

    // Update the form data state or perform any desired actions based on the checkbox change
    if (checked) {
      // Add the selected language to the languages array
      formDataM.languages.push(value);
    } else {
      // Remove the deselected language from the languages array
      const index = formDataM.languages.indexOf(value);
      if (index > -1) {
        formDataM.languages.splice(index, 1);
      }
    }
  }

  const [showPassword, setShowPassword] = useState(false);
  const [showConfirmPassword, setShowConfirmPassword] = useState(false);
  const [accountType, setAccountType] = useState("student");

  function changeHandler(event) {
    setFormData((prevData) => ({
      ...prevData,
      [event.target.name]: event.target.value,
    }));
  }
  function changeHandlerM(event) {
    setFormDataM((prevData) => ({
      ...prevData,
      [event.target.name]: event.target.value,
    }));
  }

  function submitHandler(event) {
    event.preventDefault();
    if (formData.password !== formData.confirmPassword) {
      toast.error("Passwords do not match");
      return;
    }

    const accountData = {
      ...formData,
    };

    // Convert languages array to string format
    accountData.languages = accountData.languages.join(", ");

    // Remove accountType from the accountData object
    delete accountData.accountType;

    console.log("printing Final account data ");
    console.log(accountData);
    console.log(JSON.stringify(accountData));

    fetch("http://172.20.10.3:5050/api/auth/register/mentor", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(accountData),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.mentor) {
          // Mentor registration successful
          console.log("Mentor registered successfully");
          console.log(data.mentor);
          setIsLoggedIn(true);
          toast.success("Account Created");
          navigate("/dashboard");
        } else {
          // Error occurred during mentor registration
          console.log("Mentor registration failed");
          console.log(data.message);
          // Display an error message to the user using toast or other UI mechanism
        }
      })
      .catch((error) => {
        // Error occurred during the network request
        console.log("Error occurred during mentor registration");
        console.error(error);
        // Display an error message to the user using toast or other UI mechanism
      });
  }
  function submitHandlerM(event) {
    event.preventDefault();
    if (formDataM.password !== formDataM.confirmPassword) {
      toast.error("Passwords do not match");
      return;
    }

    const accountData = {
      ...formDataM,
    };

    accountData.languages = accountData.languages.join(", ");

    // Remove accountType from the accountData object
    delete accountData.accountType;

    console.log("printing Final account data ");
    console.log(accountData);
    console.log(JSON.stringify(accountData));

    fetch("http://172.20.10.3:5050/api/auth/register/mentee", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(accountData),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.mentee) {
          // Mentor registration successful
          console.log("Mentor registered successfully");
          console.log(data.mentee);
          setIsLoggedIn(true);
          toast.success("Account Created");
          navigate("/dashboard");
        } else {
          // Error occurred during mentor registration
          console.log("Mentor registration failed");
          console.log(data.message);
          // Display an error message to the user using toast or other UI mechanism
        }
      })
      .catch((error) => {
        // Error occurred during the network request
        console.log("Error occurred during mentor registration");
        console.error(error);
        // Display an error message to the user using toast or other UI mechanism
      });
  }

  if (accountType == "instructor") {
    return (
      <div>
        {/* student-Instructor tab */}
        <div className="flex bg-richblack-800 p-1 gap-x-1 my-6 rounded-full max-w-max">
          <button
            className={`${
              accountType === "student"
                ? "bg-richblack-900 text-richblack-5"
                : "bg-transparent text-richblack-200"
            } py-2 px-5 rounded-full transition-all duration-200`}
            onClick={() => setAccountType("student")}
          >
            Mentee
          </button>

          <button
            className={`${
              accountType === "instructor"
                ? "bg-richblack-900 text-richblack-5"
                : "bg-transparent text-richblack-200"
            } py-2 px-5 rounded-full transition-all duration-200`}
            onClick={() => setAccountType("instructor")}
          >
            Mentor
          </button>
        </div>

        <form onSubmit={submitHandler}>
          {/* first name and lastName */}
          <div >
            <label>
              <p>
                Name<sup className="text-pink-200">*</sup>
              </p>
              <input
                required
                type="text"
                name="name"
                onChange={changeHandler}
                placeholder="Enter Name"
                value={formData.Name}
                className="bg-richblack-800 rounded-[0.5rem] text-richblack-5 w-full p-[12px] "
              />
            </label>

            <label className="w-full">
              <p >
                Address<sup className="text-pink-200">*</sup>
              </p>
              <input
                required
                type="text"
                name="address"
                onChange={changeHandler}
                placeholder="Enter Address"
                value={formData.address}
                className="bg-richblack-800 rounded-[0.5rem] text-richblack-5 w-full p-[12px]"
              />
            </label>
            <label className="w-full">
              <p >
                Gender<sup className="text-pink-200">*</sup>
              </p>
              <input
                required
                type="text"
                name="gender"
                onChange={changeHandler}
                placeholder="Enter Gender"
                value={formData.gender}
                className="bg-richblack-800 rounded-[0.5rem] text-richblack-5 w-full p-[12px]"
              />
            </label>
            <label className="w-full">
              <p >
                Phone Number<sup className="text-pink-200">*</sup>
              </p>
              <input
                required
                type="text"
                name="phone"
                onChange={changeHandler}
                placeholder="Enter phoneno"
                value={formData.phone}
                className="bg-richblack-800 rounded-[0.5rem] text-richblack-5 w-full p-[12px]"
              />
            </label>
            <label className="w-full">
              <p >
                Education<sup className="text-pink-200">*</sup>
              </p>
              <input
                required
                type="text"
                name="education"
                onChange={changeHandler}
                placeholder="Enter Education"
                value={formData.education}
                className="bg-richblack-800 rounded-[0.5rem] text-richblack-5 w-full p-[12px]"
              />
            </label>
          </div>
          {/* email Add */}
          <div className="mt-[20px]">
            <label className="w-full mt-[20px]">
              <p >
                Email Address<sup className="text-pink-200">*</sup>
              </p>
              <input
                required
                type="email"
                name="email"
                onChange={changeHandler}
                placeholder="Enter Email Address "
                value={formData.email}
                className="bg-richblack-800 rounded-[0.5rem] text-richblack-5 w-full p-[12px]"
              />
            </label>

            <label className="w-full">
              <p >
                Qualification<sup className="text-pink-200">*</sup>
              </p>
              <input
                required
                type="text"
                name="qualification"
                onChange={changeHandler}
                placeholder="Enter qualification"
                value={formData.qualification}
                className="bg-richblack-800 rounded-[0.5rem] text-richblack-5 w-full p-[12px]"
              />
            </label>
            <label className="w-full">
              <p >
                Date of Birth<sup className="text-pink-200">*</sup>
              </p>
              <input
                required
                type="date"
                name="dob"
                onChange={changeHandler}
                placeholder="Enter dob"
                value={formData.dob}
                className="bg-richblack-800 rounded-[0.5rem] text-richblack-5 w-full p-[12px]"
              />
            </label>
            <label className="w-full">
              <p >
                Availability<sup className="text-pink-200">*</sup>
              </p>
              <input
                required
                type="number"
                name="availability"
                onChange={changeHandler}
                placeholder="Enter availability"
                value={formData.availability}
                className="bg-richblack-800 rounded-[0.5rem] text-richblack-5 w-full p-[12px]"
              />
            </label>
          </div>

          {/* createPassword and Confirm Password */}
          <div className="w-full flex flex-col md:flex-row gap-4 mt-[20px] ">
            <label className="w-full relative">
              <p >
                Create Password<sup className="text-pink-200">*</sup>
              </p>
              <input
                required
                type={showPassword ? "text" : "password"}
                name="password"
                onChange={changeHandler}
                placeholder="Enter Password"
                value={formData.password}
                className="bg-richblack-800 rounded-[0.5rem] text-richblack-5 w-full p-[12px]"
              />
              <span
                className="absolute right-3 top-[38px] cursor-pointer"
                onClick={() => setShowPassword((prev) => !prev)}
              >
                {showPassword ? (
                  <AiOutlineEyeInvisible fontSize={24} fill="#AFB2BF" />
                ) : (
                  <AiOutlineEye fontSize={24} fill="#AFB2BF" />
                )}
              </span>
            </label>

            <label className="w-full relative">
              <p>
                Confirm Password<sup className="text-pink-200">*</sup>
              </p>
              <input
                required
                type={showConfirmPassword ? "text" : "password"}
                name="confirmPassword"
                onChange={changeHandler}
                placeholder="Confirm Password"
                value={formData.confirmPassword}
                className="bg-richblack-800 rounded-[0.5rem] text-richblack-5 w-full p-[12px]"
              />
              <span
                className="absolute right-3 top-[38px] cursor-pointer"
                onClick={() => setShowConfirmPassword((prev) => !prev)}
              >
                {showConfirmPassword ? (
                  <AiOutlineEyeInvisible fontSize={24} fill="#AFB2BF" />
                ) : (
                  <AiOutlineEye fontSize={24} fill="#AFB2BF" />
                )}
              </span>
            </label>
            <div>
              <label className="w-full">
                <p >
                  kannada
                </p>
                <input
                  type="checkbox"
                  name="kannada"
                  value="kannada"
                  onChange={checkboxChangeHandler}
                />
              </label>
              <label className="w-full">
                <p>
                  telugu
                </p>
                <input
                  type="checkbox"
                  name="telugu"
                  value="telugu"
                  onChange={checkboxChangeHandler}
                />
              </label>
              <label className="w-full">
                <p >
                  tamil
                </p>
                <input
                  type="checkbox"
                  name="tamil"
                  value="tamil"
                  onChange={checkboxChangeHandler}
                />
              </label>
              <label className="w-full">
                <p >
                  hindi
                </p>
                <input
                  type="checkbox"
                  name="hindi"
                  value="hindi"
                  onChange={checkboxChangeHandler}
                />
              </label>
              <label className="w-full">
                <p >
                  english
                </p>
                <input
                  type="checkbox"
                  name="english"
                  value="english"
                  onChange={checkboxChangeHandler}
                />
              </label>
            </div>
          </div>
          <button className=" w-full bg-yellow-50 rounded-[8px] font-medium text-richblack-900 px-[12px] py-[8px] mt-6">
            Create Account
          </button>
        </form>
      </div>
    );
  } else {
    return (
      <div>
        {/* student-Instructor tab */}
        <div className="flex bg-richblack-800 p-1 gap-x-1 my-6 rounded-full max-w-max">
          <button
            className={`${
              accountType === "student"
                ? "bg-richblack-900 text-richblack-5"
                : "bg-transparent text-richblack-200"
            } py-2 px-5 rounded-full transition-all duration-200`}
            onClick={() => setAccountType("student")}
          >
            Mentee
          </button>

          <button
            className={`${
              accountType === "instructor"
                ? "bg-richblack-900 text-richblack-5"
                : "bg-transparent text-richblack-200"
            } py-2 px-5 rounded-full transition-all duration-200`}
            onClick={() => setAccountType("instructor")}
          >
            Mentor
          </button>
        </div>

        <form onSubmit={submitHandlerM}>
          {/* first name and lastName */}
          <div className="flex flex-col md:flex-row gap-4 mt-[20px]">
            <label className="w-full">
              <p >
                Name <sup className="text-pink-200">*</sup>
              </p>
              <input
                required
                type="text"
                name="name"
                onChange={changeHandlerM}
                placeholder="Enter Name"
                value={formDataM.name}
                className="bg-richblack-800 rounded-[0.5rem] text-richblack-5 w-full p-[12px] "
              />
            </label>

            <label className="w-full">
              <p >
                Address<sup className="text-pink-200">*</sup>
              </p>
              <input
                required
                type="text"
                name="address"
                onChange={changeHandlerM}
                placeholder="Enter Address"
                value={formDataM.address}
                className="bg-richblack-800 rounded-[0.5rem] text-richblack-5 w-full p-[12px]"
              />
            </label>
            <label className="w-full">
              <p >
                Phone Number<sup className="text-pink-200">*</sup>
              </p>
              <input
                required
                type="text"
                name="phone"
                onChange={changeHandlerM}
                placeholder="Enter phoneno"
                value={formDataM.phoneno}
                className="bg-richblack-800 rounded-[0.5rem] text-richblack-5 w-full p-[12px]"
              />
            </label>
            <label className="w-full">
              <p >
                Education<sup className="text-pink-200">*</sup>
              </p>
              <input
                required
                type="text"
                name="education"
                onChange={changeHandlerM}
                placeholder="Enter Education"
                value={formData.educationM}
                className="bg-richblack-800 rounded-[0.5rem] text-richblack-5 w-full p-[12px]"
              />
            </label>
          </div>
          {/* email Add */}
          <div className="mt-[20px]">
            <label className="w-full mt-[20px]">
              <p >
                Email Address<sup className="text-pink-200">*</sup>
              </p>
              <input
                required
                type="email"
                name="email"
                onChange={changeHandlerM}
                placeholder="Enter Email Address "
                value={formDataM.email}
                className="bg-richblack-800 rounded-[0.5rem] text-richblack-5 w-full p-[12px]"
              />
            </label>
          </div>

          {/* createPassword and Confirm Password */}
          <div className="w-full flex flex-col md:flex-row gap-4 mt-[20px] ">
            <label className="w-full relative">
              <p >
                Create Password<sup className="text-pink-200">*</sup>
              </p>
              <input
                required
                type={showPassword ? "text" : "password"}
                name="password"
                onChange={changeHandlerM}
                placeholder="Enter Password"
                value={formDataM.password}
                className="bg-richblack-800 rounded-[0.5rem] text-richblack-5 w-full p-[12px]"
              />
              <span
                className="absolute right-3 top-[38px] cursor-pointer"
                onClick={() => setShowPassword((prev) => !prev)}
              >
                {showPassword ? (
                  <AiOutlineEyeInvisible fontSize={24} fill="#AFB2BF" />
                ) : (
                  <AiOutlineEye fontSize={24} fill="#AFB2BF" />
                )}
              </span>
            </label>

            <label className="w-full relative">
              <p >
                Confirm Password<sup className="text-pink-200">*</sup>
              </p>
              <input
                required
                type={showConfirmPassword ? "text" : "password"}
                name="confirmPassword"
                onChange={changeHandlerM}
                placeholder="Confirm Password"
                value={formDataM.confirmPassword}
                className="bg-richblack-800 rounded-[0.5rem] text-richblack-5 w-full p-[12px]"
              />
              <span
                className="absolute right-3 top-[38px] cursor-pointer"
                onClick={() => setShowConfirmPassword((prev) => !prev)}
              >
                {showConfirmPassword ? (
                  <AiOutlineEyeInvisible fontSize={24} fill="#AFB2BF" />
                ) : (
                  <AiOutlineEye fontSize={24} fill="#AFB2BF" />
                )}
              </span>
            </label>
            <div>
              <label className="w-full">
                <p >
                  kannada
                </p>
                <input
                  type="checkbox"
                  name="kannada"
                  value="kannada"
                  onChange={checkboxChangeHandlerM}
                />
              </label>
              <label className="w-full">
                <p >
                  telugu
                </p>
                <input
                  type="checkbox"
                  name="telugu"
                  value="telugu"
                  onChange={checkboxChangeHandlerM}
                />
              </label>
              <label className="w-full">
                <p >
                  tamil
                </p>
                <input
                  type="checkbox"
                  name="tamil"
                  value="tamil"
                  onChange={checkboxChangeHandlerM}
                />
              </label>
              <label className="w-full">
                <p >
                  hindi
                </p>
                <input
                  type="checkbox"
                  name="hindi"
                  value="hindi"
                  onChange={checkboxChangeHandlerM}
                />
              </label>
              <label className="w-full">
                <p >
                  english
                </p>
                <input
                  type="checkbox"
                  name="english"
                  value="english"
                  onChange={checkboxChangeHandlerM}
                />
              </label>
            </div>
          </div>
          <button className=" w-full bg-yellow-50 rounded-[8px] font-medium text-richblack-900 px-[12px] py-[8px] mt-6">
            Create Account
          </button>
        </form>
      </div>
    );
  }
};
export default SignupForm;
