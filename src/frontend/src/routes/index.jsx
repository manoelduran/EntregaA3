import React from 'react';
import { Route, Routes } from 'react-router-dom';
import Home from '../pages/Home';
import CustomersDashboard from '../pages/CustomersDashboard';
import ProductsDashboard from '../pages/ProductsDashboard';
import OrdersDashboard from '../pages/OrdersDashboard';
import CreateOrUpdateCustomer from '../pages/CreateOrUpdateCustomer';
import CustomerDetails from '../pages/CustomerDetails';

const AppRoutes = () => {
  return (
    <Routes >
      <Route path="/" exact element={<Home />} />
      <Route path="/customers" element={<CustomersDashboard />} />
      <Route path="/customers/create" exact element={<CreateOrUpdateCustomer />} />
      <Route path="/customers/:id/edit" exact element={<CreateOrUpdateCustomer />} />
      <Route path="/customers/:id/show" element={<CustomerDetails />} />
      <Route path="/products" element={<ProductsDashboard />} />
      <Route path="/orders" element={<OrdersDashboard />} />
    </Routes>
  );
};

export default AppRoutes;
