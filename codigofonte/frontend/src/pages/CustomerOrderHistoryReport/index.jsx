import React, { useState, useEffect, useMemo } from "react";
import Button from "../../components/Button";
import "./styles.css";
import { api } from "../../services/api";
import { useNavigate, useLocation } from "react-router-dom";

const CustomerOrderHistoryReport = () => {
  const { state } = useLocation();
  const navigate = useNavigate();
  const customer = state && state.customer;
  const [orders, setOrders] = useState([]);
  const [error, setError] = useState('')
  useEffect(() => {
    api
      .get(`/orders/customer/${customer.id}`)
      .then((response) => {

        if (typeof response.data === 'string') {
          setError(response.data)
          return
        }
        setOrders(response.data);
      })
      .catch((error) =>
        console.error("Erro ao buscar histórico de pedidos:", error)
      );
  }, []);

  const formattedOrders = useMemo(() => {
    if (orders.length === 0 && error) {
      return
    }
    const map = {};

    orders.forEach((order) => {
      const { product_id, quantity } = order;

      if (map[product_id]) {
        map[product_id].quantity += quantity;
      } else {
        map[product_id] = { ...order };
      }
    });
    const list = Object.values(map);

    return list.map((item) => ({
      ...item,
      total: item.price * item.quantity,
    }));
  }, [orders]);
  if (error) return (<div style={{ width: '100%', height: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '5px' }}>
    <h1>{error}</h1>
    <Button title='Voltar' onClick={() => navigate(-1)} />
  </div>)
  return (
    <div className="table-container">
      <div className="table-header">
        <h2 className="table-title">
          Histórico de Pedidos de {customer?.name}
        </h2>
        <div className="table-actions">
          <Button onClick={() => navigate(-1)} title="Voltar" color="#808080" />
        </div>
      </div>
      <table>
        <thead>
          <tr>
            <th>ID do Pedido</th>
            <th>ID do Produto</th>
            <th>Nome do Produto</th>
            <th>Valor Unitário</th>
            <th>Quantidade Total</th>
            <th>Valor Total</th>
            <th>Data de Compra</th>
          </tr>
        </thead>
        <tbody>
          {formattedOrders?.map((order) => (
            <tr key={order.id}>
              <td>{order.id}</td>
              <td>{order.product_id}</td>
              <td>{order.product_name}</td>
              <td>R$ {order.price}</td>
              <td>{order.quantity}</td>
              <td>R$ {order.total}</td>
              <td>{order.ordered_at}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default CustomerOrderHistoryReport;
