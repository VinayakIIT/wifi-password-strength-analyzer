# WiFi Security Analyzer
Website Link- https://vinayakiit.github.io/wifi-password-strength-analyzer/
A web-based tool for evaluating the strength of WiFi passwords. The frontend provides a user-friendly interface to enter passwords and visualize analysis results, while a Python Flask backend performs robust password strength checks including length, complexity, entropy, common pattern detection, and breach simulation.

---

## Table of Contents

- [Project Overview](#project-overview)  
- [Features](#features)  
- [Technology Stack](#technology-stack)  
- [Setup and Installation](#setup-and-installation)  
- [Usage](#usage)  
- [Security & Privacy](#security--privacy)  
- [Troubleshooting](#troubleshooting)  
- [Future Enhancements](#future-enhancements)
## Project Overview

WiFi networks are ubiquitous, but many remain vulnerable due to weak passwords. This project helps users assess the security of their WiFi passwords with detailed feedback and actionable improvement suggestions, balancing usability and security.

The password analysis is executed on a Python Flask backend to ensure consistent, accurate computation and encapsulation of sensitive logic, while the frontend leverages TailwindCSS and Chart.js for an intuitive, responsive user experience.

---

## Features

### Comprehensive Password Strength Analysis

- **Length Assessment:** Encourages secure minimum password length (ideally 12+ characters).  
- **Character Variety Checks:** Detects uppercase, lowercase, numbers, and special symbols.  
- **Entropy Calculation:** Computes Shannon entropy as an indicator of password randomness.  
- **Common Password Detection:** Flags common (likely compromised) passwords from a built-in list.  
- **Pattern Recognition:** Identifies sequential patterns ("123", "abc") and repeated characters ("aaa") that weaken security.  
- **Overall Strength Scoring:** Combines factors into an intuitive 0–100 strength score.

### User-Friendly and Privacy-Focused UI

- **Real-time Feedback:** Visual color-coded strength meter with dynamic updates.  
- **Improvement Tips:** Contextual, actionable advice displayed based on detected weaknesses.  
- **Security Visualization:** Interactive bar chart highlighting key strength factors.  
- **Password Visibility Toggle:** Easily show/hide password input for user convenience.  
- **Accessibility:** ARIA labels and keyboard support for improved usability.

### Secure Python Flask Backend

- **Robust Logic:** Centralized, tested password analysis logic implemented in Python.  
- **RESTful JSON API:** Simple `/analyze` POST endpoint for password evaluation.  
- **Cross-Origin Resource Sharing (CORS):** Configured to enable frontend-backend communication during development.

### Privacy & Security

- **Local Analysis:** Passwords are analyzed and discarded locally; no logs or persistent storage.  
- **No External APIs:** Does not transmit passwords to third parties.  
- **Open Source:** Full transparency of analysis methodology.  
- **Ready for Expansion:** Designed to support privacy-preserving external breach checks or advanced algorithms.

### Responsive Modern Frontend

- **TailwindCSS for Styling:** Clean, responsive UI that works on desktop and mobile devices.  
- **Chart.js for Visualization:** Clear graphical representation of analysis results.  
- **Lightweight:** Minimal dependencies for fast load and smooth interactions.

---

## Technology Stack

| Layer       | Technology                          |
|-------------|-----------------------------------|
| Frontend    | HTML, CSS (TailwindCSS), JavaScript |
| Password Visualization | Chart.js                |
| Backend     | Python 3 with Flask and Flask-CORS |

---

## Setup and Installation

### Prerequisites

- Python 3.7+ installed  
- `pip` Python package manager  
- Modern web browser (Chrome, Firefox, Edge, Safari)

### Backend Setup
i have created a automated backend server that deploy automactically when we start the website at render.com
my render link is also here 
https://wifi-password-strength-analyzer.onrender.com
### Frontend Setup

- Simply **open `index.html`** (or the provided HTML file) with your preferred browser.  
- No additional server needed for frontend when running locally.

---

## Usage

1. Open `index.html` in a web browser.

2. Enter your WiFi password in the input field.

3. Click **Analyze Security**.

4. The frontend will send the password securely to the backend.

5. The backend analyzes the password and sends back detailed metrics:

- Password length and character variety  
- Entropy calculation  
- Common password detection  
- Sequential and repeated pattern identification  
- Overall numeric strength score (0–100)  

6. Visual feedback is presented:

- Color-coded strength meter  
- Icon indicators  
- Improvement tips tailored to specific issues  
- Security factor bar chart visualization  

7. Modify your password based on feedback for improved security.

---

## Security & Privacy

- Passwords are **analyzed locally** on the backend instance you run.  
- No data is stored, logged, or sent to external services.  
- Communication between frontend and backend is local (`localhost`) by default.  
- For production deployment, secure your backend with HTTPS and authentication.  
- No third-party APIs are called, enhancing privacy.

---

## Troubleshooting

| Issue                              | Potential Cause                        | Solution                                         |
|-----------------------------------|-------------------------------------|------------------------------------------------|
| CORS errors in browser console    | Backend missing CORS headers         | Ensure `flask-cors` is installed and enabled in `app.py`. |
| “Failed to fetch” or network error | Backend server not running or wrong port | Start backend with `python app.py`; confirm URL and port in frontend. |
| 404 or endpoint not found         | Mismatch in frontend/backend route   | Ensure frontend JS sends POST to `/analyze` endpoint on correct port. |
| No response or UI freezes         | Backend crashed / Exception thrown   | Check backend terminal logs; debug exceptions. |
| Browser cache shows old frontend  | Cached JS or CSS artifacts            | Hard refresh page using Ctrl+Shift+R or clear cache. |

---

## Future Enhancements

- Integration with privacy-aware breach databases (e.g., HaveIBeenPwned k-anonymity API).  
- Implement advanced password strength estimator libraries (e.g., Dropbox `zxcvbn`).  
- Add user authentication and HTTPS for secure remote deployment.  
- Accessibility improvements beyond ARIA labels (screen reader testing).  
- Mobile-specific UI optimizations and progressive web app support.  
- Dockerize the backend for easier containerized deployment.
