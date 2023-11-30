import React from "react";
import { Route, Routes } from "react-router-dom";
import Home from "../pages/Home";
import CustomersDashboard from "../pages/CustomersDashboard";
import ProductsDashboard from "../pages/ProductsDashboard";
import OrdersDashboard from "../pages/OrdersDashboard";
import CreateOrUpdateCustomer from "../pages/CreateOrUpdateCustomer";
import CustomerDetails from "../pages/CustomerDetails";
import ProductsDetails from "../pages/ProductsDetails";
import CreateOrUpdateProduct from "../pages/CreateOrUpdateProduct";
import OrderDetails from "../pages/OrderDetails";
import CreateOrUpdateOrder from "../pages/CreateOrUpdateOrder";
import CustomerOrderHistoryReport from "../pages/CustomerOrderHistoryReport";
import CustomerAverage from "../pages/CustomerAverage";
import ProductsBestsellers from "../pages/ProductsBestsellers";

const AppRoutes = () => {
  return (
    <Routes>
      <Route path="/" exact element={<Home />} />
      <Route path="/customers" element={<CustomersDashboard />} />
      <Route
        path="/customers/create"
        exact
        element={<CreateOrUpdateCustomer />}
      />
      <Route
        path="/customers/:id/edit"
        exact
        element={<CreateOrUpdateCustomer />}
      />
      <Route path="/customers/:id/show" element={<CustomerDetails />} />
      <Route path="/products" element={<ProductsDashboard />} />
      <Route
        path="/products/create"
        exact
        element={<CreateOrUpdateProduct />}
      />
      <Route path="/products/:id/show" element={<ProductsDetails />} />
      <Route path="/products/bestsellers" element={<ProductsBestsellers />} />
      <Route
        path="/products/:id/edit"
        exact
        element={<CreateOrUpdateProduct />}
      />
      <Route path="/orders" element={<OrdersDashboard />} />
      <Route path="/orders/create" exact element={<CreateOrUpdateOrder />} />
      <Route path="/orders/:id/show" exact element={<OrderDetails />} />
      <Route
        path="/orders/customer/:id"
        element={<CustomerOrderHistoryReport />}
      />
      <Route
        path="/orders/customer/:id/average"
        element={<CustomerAverage />}
      />
      <Route path="/orders/:id/edit" exact element={<CreateOrUpdateOrder />} />
    </Routes>
  );
};

export default AppRoutes;
