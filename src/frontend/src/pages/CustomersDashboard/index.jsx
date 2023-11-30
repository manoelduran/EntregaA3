import React, { useState, useEffect } from "react";
import Button from "../../components/Button";
import "./styles.css";
import { api } from "../../services/api";
import { useNavigate } from "react-router-dom";

const CustomersDashboard = () => {
  const navigate = useNavigate();
  const [customers, setCustomers] = useState([]);

  useEffect(() => {
    api
      .get("/customers")
      .then((response) => {
        setCustomers(response.data);
      })
      .catch((error) => console.error("Erro ao buscar clientes:", error));
  }, []);
  const handleView = (customerId) => {
    navigate(`/customers/${customerId}/show`, { state: { customerId } });
  };
  const handleOrderHistory = (customer) => {
    navigate(`/orders/customer/${customer.id}`, {
      state: { customer },
    });
  };
  const handleDelete = (customerId) => {
    api
      .delete(`/customers/${customerId}`)
      .catch((error) => console.error("Erro ao buscar clientes:", error));
    api
      .get("/customers")
      .then((response) => {
        setCustomers(response.data);
      })
      .catch((error) => console.error("Erro ao buscar clientes:", error));
  };
  const handleCustomerAverage = (customer) => {
    navigate(`/orders/customer/${customer.id}/average`, {
      state: { customer },
    });
  };
  const handleUpdate = (customerId) => {
    navigate(`/customers/${customerId}/edit`, { state: { customerId } });
  };
  return (
    <div className="table-container">
      <div className="table-header">
        <h2 className="table-title">Lista de Clientes</h2>
        <div className="table-actions">
          <Button
            onClick={() => navigate("/customers/create")}
            title="Criar Cliente"
            color="#808080"
          />
          <Button onClick={() => navigate(-1)} title="Voltar" color="#808080" />
        </div>
      </div>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Nome</th>
            <th>E-mail</th>
            <th>Senha</th>
            <th>Data de Criação</th>
            <th>Ações</th>
          </tr>
        </thead>
        <tbody>
          {customers.map((customer) => (
            <tr key={customer.id}>
              <td>{customer.id}</td>
              <td>{customer.name}</td>
              <td>{customer.email}</td>
              <td>{customer.password}</td>
              <td>{customer.created_at}</td>
              <td>
                <Button
                  onClick={() => handleView(customer.id)}
                  title="Visualizar"
                  color="#007BFF"
                />
                <Button
                  onClick={() => handleDelete(customer.id)}
                  title="Deletar"
                  color="#DC3545"
                />
                <Button
                  onClick={() => handleUpdate(customer.id)}
                  title="Atualizar"
                  color="#4CAF50"
                />
                <Button
                  onClick={() => handleOrderHistory(customer)}
                  title="Histórico de Pedidos"
                  color="#FFA500"
                />
                <Button
                  onClick={() => handleCustomerAverage(customer)}
                  title="Consumo Médio"
                  color="#FFA500"
                />
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default CustomersDashboard;
