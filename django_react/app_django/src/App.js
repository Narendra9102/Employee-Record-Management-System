import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import RegistrationForm from './components/RegistrationForm';
import LoginForm from './components/LoginForm';
import Customer from './components/Customer';

function App() {
  return (
    <div className='App'>
      <Router>
        <Routes>
          <Route path='/' element={<RegistrationForm />} />
          <Route path='login' element={<LoginForm />} />
          <Route path='customer' element={<Customer />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
