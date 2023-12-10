import React, { useState, useEffect, useMemo } from "react";
import Button from "../../components/Button";
import "./styles.css";
import { api } from "../../services/api";
import { useNavigate } from "react-router-dom";

const ProductsBestsellers = () => {
  const navigate = useNavigate();
  const [orders, setOrders] = useState([]);
  const [error, setError] = useState('')
  useEffect(() => {
    api
      .get("/orders/products")
      .then((response) => {

        if (typeof response.data === 'string') {
          setError(response.data)
          return
        }
        setOrders(response.data)
      })
      .catch((error) => console.error("Erro ao buscar produtos:", error));
  }, []);
  const productsBestSellers = useMemo(() => {
    if (orders.length === 0 && error) {
      return
    }
    const productsCounter = {};
    orders?.forEach((order) => {
      const { product_id, product_name, price } = order;
      if (!productsCounter[product_id]) {
        productsCounter[product_id] = {
          totalQuantity: 0,
          product_name,
          price,
        };
      }
      productsCounter[product_id].totalQuantity += 1;
    });
    const products = Object.keys(productsCounter).map((product_id) => ({
      product_id,
      ...productsCounter[product_id],
    }));
    const sortedProducts = products.sort(
      (a, b) => b.totalQuantity - a.totalQuantity
    );
    return sortedProducts;
  }, [orders]);

  if (error) return (<div style={{ width: '100%', height: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '5px' }}>
    <h1>{error}</h1>
    <Button title='Voltar' onClick={() => navigate(-1)} />
  </div>)
  return (
    <div className="table-container">
      <div className="table-header">
        <h2 className="table-title">Produtos Mais Vendidos</h2>
        <div className="table-actions">
          <Button onClick={() => navigate(-1)} title="Voltar" color="#808080" />
        </div>
      </div>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Nome</th>
            <th>Preço</th>
            <th>Quantidade</th>
          </tr>
        </thead>
        <tbody>
          {productsBestSellers?.map((product) => (
            <tr key={product.product_id}>
              <td>{product.product_id}</td>
              <td>{product.product_name}</td>
              <td>R$ {product.price}</td>
              <td>{product.totalQuantity}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ProductsBestsellers;
