import React, { useState } from 'react';
import './Register.css';


const Register = () => {
  const [userType, setUserType] = useState(null);
  const [selectedLanguages, setSelectedLanguages] = useState([]);

  const handleButtonClick = (type) => {
    setUserType(type);
  };

  const handleLanguageChange = (event) => {
    const { value, checked } = event.target;
    if (checked) {
      setSelectedLanguages((prevLanguages) => [...prevLanguages, value]);
    } else {
      setSelectedLanguages((prevLanguages) =>
        prevLanguages.filter((lang) => lang !== value)
      );
    }
  };

  const renderForm = () => {
    if (userType === 'mentor') {
      return (
        <form>
          <label>
            Name:
            <input type="text" />
          </label><br />
          <label>
            Date of Birth:
            <input type="date" />
          </label><br />
          <label>
            Email:
            <input type="email" />
          </label><br />
          <label>
            Phone:
            <input type="tel" />
          </label><br />
          <label>
            Address:
            <input type="text" />
          </label><br />
          <label>
            Gender:
            <input type="text" />
          </label><br />
          <label>
            Degree:
            <input type="text" />
          </label><br />
          <label>
            Password:
            <input type="password" />
          </label><br />
          <label>
            Company:
            <input type="text" />
          </label><br />
          <label>
            Language:
            <div>
              <label>
                <input
                  type="checkbox"
                  value="hindi"
                  checked={selectedLanguages.includes('hindi')}
                  onChange={handleLanguageChange}
                />
                Hindi
              </label>
              <label>
                <input
                  type="checkbox"
                  value="english"
                  checked={selectedLanguages.includes('english')}
                  onChange={handleLanguageChange}
                />
                English
              </label>
              <label>
                <input
                  type="checkbox"
                  value="marathi"
                  checked={selectedLanguages.includes('kannada')}
                  onChange={handleLanguageChange}
                />
                Kannada
              </label>
              <label>
                <input
                  type="checkbox"
                  value="marathi"
                  checked={selectedLanguages.includes('tulu')}
                  onChange={handleLanguageChange}
                />
                Tulu
              </label>
              <label>
                <input
                  type="checkbox"
                  value="marathi"
                  checked={selectedLanguages.includes('telegu')}
                  onChange={handleLanguageChange}
                />
                Telegu
              </label>
              <label>
                <input
                  type="checkbox"
                  value="marathi"
                  checked={selectedLanguages.includes('tamil')}
                  onChange={handleLanguageChange}
                />
                Tamil
              </label>
              <label>
                <input
                  type="checkbox"
                  value="marathi"
                  checked={selectedLanguages.includes('marathi')}
                  onChange={handleLanguageChange}
                />
                Marathi
              </label>
            </div>
          </label>
          <button type="submit">Register</button>
        </form>
      );
    }

    if (userType === 'mentee') {
      return (
        <form>
          <label>
            Name:
            <input type="text" />
          </label><br />
          <label>
            Date of Birth:
            <input type="date" />
          </label><br />
          <label>
            Email:
            <input type="email" />
          </label><br />
          <label>
            College:
            <input type="text" />
          </label><br />
          <label>
            Phone:
            <input type="tel" />
          </label><br />
          <label>
            Password:
            <input type="password" />
          </label><br />
          <label>
            Address:
            <input type="text" />
          </label><br />
          <label>
            Gender:
            <input type="text" default="F" />
          </label><br />
          <label>
            Education:
            <input type="text" />
          </label><br />
          <label>
            Language:
            <div>
              <label>
                <input
                  type="checkbox"
                  value="hindi"
                  checked={selectedLanguages.includes('hindi')}
                  onChange={handleLanguageChange}
                />
                Hindi
              </label>
              <label>
                <input
                  type="checkbox"
                  value="english"
                  checked={selectedLanguages.includes('english')}
                  onChange={handleLanguageChange}
                />
                English
              </label>
              <label>
                <input
                  type="checkbox"
                  value="marathi"
                  checked={selectedLanguages.includes('kannada')}
                  onChange={handleLanguageChange}
                />
                Kannada
              </label>
              <label>
                <input
                  type="checkbox"
                  value="marathi"
                  checked={selectedLanguages.includes('tulu')}
                  onChange={handleLanguageChange}
                />
                Tulu
              </label>
              <label>
                <input
                  type="checkbox"
                  value="marathi"
                  checked={selectedLanguages.includes('telegu')}
                  onChange={handleLanguageChange}
                />
                Telegu
              </label>
              <label>
                <input
                  type="checkbox"
                  value="marathi"
                  checked={selectedLanguages.includes('tamil')}
                  onChange={handleLanguageChange}
                />
                Tamil
              </label>
              <label>
                <input
                  type="checkbox"
                  value="marathi"
                  checked={selectedLanguages.includes('marathi')}
                  onChange={handleLanguageChange}
                />
                Marathi
              </label>
              {/* Add more language options as needed */}
            </div>
          </label>
          <button type="submit">Register</button>
        </form>
      );
    }

    return null;
  };

  return (
    <div>
      <button onClick={() => handleButtonClick('mentor')}>Mentor</button>
      <button onClick={() => handleButtonClick('mentee')}>Mentee</button>
      {renderForm()}
    </div>
  );
};

export default Register;
