import React, { useState, useEffect } from "react";
import Button from "../../components/Button";
import "./styles.css";
import { api } from "../../services/api";
import { useNavigate } from "react-router-dom";
const OrdersDashboard = () => {
  const navigate = useNavigate();
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    api
      .get("/orders")
      .then((response) => setOrders(response.data))
      .catch((error) => console.error("Erro ao buscar pedidos:", error));
  }, []);
  const handleView = (orderId) => {
    navigate(`/orders/${orderId}/show`, { state: { orderId } });
  };

  const handleDelete = (orderId) => {
    api
      .delete(`/orders/${orderId}`)
      .then(() => {
        api
          .get("/orders")
          .then((response) => {
            setOrders(response.data);
          })
          .catch((error) => console.error("Erro ao buscar pedidos:", error));
      })
      .catch((error) => console.error("Erro ao buscar pedidos:", error));
  };

  const handleUpdate = (orderId) => {
    navigate(`/orders/${orderId}/edit`, { state: { orderId } });
  };
  return (
    <div className="table-container">
      <div className="table-header">
        <h2 className="table-title">Lista de Pedidos</h2>
        <div className="table-actions">
          <Button
            onClick={() => navigate("/orders/create")}
            title="Criar Pedido"
            color="#808080"
          />
          <Button onClick={() => navigate(-1)} title="Voltar" color="#808080" />
        </div>
      </div>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>ID do Customer</th>
            <th>Método de Pagamento</th>
            <th>ID do Produto</th>
            <th>Quantidade</th>
            <th>Dia da Criação do Pedido</th>
            <th>Ações</th>
          </tr>
        </thead>
        <tbody>
          {orders.map((order) => (
            <tr key={order.id}>
              <td>{order.id}</td>
              <td>{order.customer_id}</td>
              <td>{order.payment_method}</td>
              <td>{order.product_id}</td>
              <td>{order.quantity}</td>
              <td>{order.ordered_at}</td>
              <td>
                <Button
                  onClick={() => handleView(order.id)}
                  title="Visualizar"
                  color="#007BFF"
                />
                <Button
                  onClick={() => handleDelete(order.id)}
                  title="Deletar"
                  color="#DC3545"
                />
                <Button
                  onClick={() => handleUpdate(order.id)}
                  title="Atualizar"
                  color="#4CAF50"
                />
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default OrdersDashboard;
