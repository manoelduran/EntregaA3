import React, { useState, useEffect } from "react";
import { useNavigate, useLocation } from "react-router-dom";
import { api } from "../../services/api";
import Button from "../../components/Button";
import "./styles.css";

const CreateOrUpdateOrder = () => {
  const { state } = useLocation();
  const navigate = useNavigate();
  const orderId = state && state.orderId;

  const [order, setOrder] = useState({
    customer_id: 0,
    payment_method: "",
    product_id: 0,
    quantity: 0,
  });
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  useEffect(() => {
    if (!!orderId) {
      setLoading(true);
      api
        .get(`/orders/${orderId}`)
        .then((response) => {
          setOrder(response.data);
          setLoading(false);
        })
        .catch((error) => console.error("Erro ao buscar pedidos:", error));
    }
  }, []);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setOrder((prevProduct) => ({
      ...prevProduct,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    try {
      e.preventDefault();
      if (orderId) {
        const formData = new FormData(e.target);
        const orderData = {};

        formData.forEach((value, key) => {
          orderData[key] = value;
        });
        await api.put(`/orders/${orderId}`, orderData);
        navigate("/orders");
      } else {
        const formData = new FormData(e.target);
        const orderData = {};

        formData.forEach((value, key) => {
          orderData[key] = value;
        });
        await api.post("/orders", orderData);
        navigate("/orders");
      }
    } catch (error) {
      setError(error.response.data.detail);
    }
  };
  if (loading) {
    return (
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
        <Button title="Voltar" onClick={() => navigate(-1)} />
      </div>
    );
  }
  if (error) {
    return (
      <>
        <div className="title-container">
          <h1>{orderId ? "Atualizar Pedido" : "Criar Pedido"}</h1>
          <Button title="Voltar" onClick={() => navigate(-1)} />
        </div>
        <div
          style={{
            width: "100%",
            height: "100vh",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
          }}
        >
          Error: {error}
        </div>
      </>
    );
  }
  return (
    <div className="container">
      <div className="title-container">
        <h1>{orderId ? "Atualizar Pedido" : "Criar Pedido"}</h1>
        <Button title="Voltar" onClick={() => navigate(-1)} />
      </div>

      <form onSubmit={handleSubmit}>
        <label>
          Cliente:
          <input
            type="text"
            name="customer_id"
            value={order.customer_id}
            onChange={handleChange}
          />
        </label>
        <label>
          Método de Pagamento:
          <input
            type="text"
            name="payment_method"
            value={order.payment_method}
            onChange={handleChange}
          />
        </label>
        <label>
          Produto:
          <input
            type="text"
            name="product_id"
            value={order.product_id}
            onChange={handleChange}
          />
        </label>
        <label>
          Quantidade:
          <input
            type="number"
            name="quantity"
            value={order.quantity}
            onChange={handleChange}
          />
        </label>
        <Button title={orderId ? "Atualizar" : "Criar"} type="submit" />
      </form>
    </div>
  );
};

export default CreateOrUpdateOrder;
