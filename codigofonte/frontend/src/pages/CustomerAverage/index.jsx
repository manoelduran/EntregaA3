import React, { useEffect, useState, useMemo } from "react";
import "./styles.css";
import { useLocation, useNavigate } from "react-router-dom";
import { api } from "../../services/api";
import Button from "../../components/Button";

const CustomerAverage = () => {
  const { state } = useLocation();
  const navigate = useNavigate();
  const customer = state && state.customer;
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    api
      .get(`/orders/customer/${customer.id}`)
      .then((response) => {
        setOrders(response.data);
      })
      .catch((error) => console.error("Erro ao buscar pedidos:", error));
  }, []);
  const formattedOrders = useMemo(() => {
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
  const totalSum = formattedOrders?.reduce((acc, item) => acc + item.total, 0);
  return (
    <div className="container">
      {Boolean(orders) ? (
        <>
          <div className="title-container">
            <h1>Consumo Médio do {customer.name}</h1>
            <Button title="Voltar" onClick={() => navigate(-1)} />
          </div>
          <div className="customer-details">
            <p>
              <strong>Nome:</strong> {customer.name}
            </p>
            <p>
              <strong>Total de pedidos realizados:</strong> {orders.length}
            </p>
            <p>
              <strong>Total gasto:</strong> R$ {totalSum}
            </p>
            <p>
              <strong>Consumo médio:</strong> R$ {totalSum / orders.length}
            </p>
          </div>
        </>
      ) : (
        <div
          style={{
            width: "100%",
            height: "100vh",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
          }}
        >
          Carregando...
        </div>
      )}
    </div>
  );
};

export default CustomerAverage;
