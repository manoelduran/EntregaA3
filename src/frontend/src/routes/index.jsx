import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from '../pages/Home';
import CustomersDashboard from '../pages/CustomersDashboard';
import ProductsDashboard from '../pages/ProductsDashboard';
import OrdersDashboard from '../pages/OrdersDashboard';

const AppRoutes = () => {
  return (
    <Routes >
        <Route path="/" exact element={<Home/>} />
        <Route path="/customers" element={<CustomersDashboard/>} />
        <Route path="/products" element={<ProductsDashboard/>} />
        <Route path="/orders" element={<OrdersDashboard/>} />
    </Routes>
  );
};

export default AppRoutes;
