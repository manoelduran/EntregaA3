import React, { useState, useEffect } from "react";
import Button from "../../components/Button";
import "./styles.css";
import { api } from "../../services/api";
import { useNavigate } from "react-router-dom";

const ProductsDashboard = () => {
  const navigate = useNavigate();
  const [products, setProducts] = useState([]);

  useEffect(() => {
    api
      .get("/products")
      .then((response) => setProducts(response.data))
      .catch((error) => console.error("Erro ao buscar produtos:", error));
  }, []);
  const handleView = (productId) => {
    navigate(`/products/${productId}/show`, { state: { productId } });
  };
  const handleDelete = (customerId) => {
    api
      .delete(`/products/${customerId}`)
      .catch((error) => console.error("Erro ao buscar clientes:", error));
    api
      .get("/products")
      .then((response) => {
        setProducts(response.data);
      })
      .catch((error) => console.error("Erro ao buscar clientes:", error));
  };

  const handleUpdate = (productId) => {
    navigate(`/products/${productId}/edit`, { state: { productId } });
  };
  return (
    <div className="table-container">
      <div className="table-header">
        <h2 className="table-title">Lista de Produtos</h2>
        <div className="table-actions">
          <Button
            onClick={() => navigate("/products/create")}
            title="Criar Produto"
            color="#808080"
          />
          <Button
            onClick={() => navigate(`/products/bestsellers`)}
            title="Mais Vendidos"
            color="#808080"
          />
          <Button
            onClick={() => navigate(`/products/low-stock`)}
            title="Baixo Estoque"
            color="#FF69B4"
          />
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
            <th>Data de Criação</th>
            <th>Ações</th>
          </tr>
        </thead>
        <tbody>
          {products.map((product) => (
            <tr key={product.id}>
              <td>{product.id}</td>
              <td>{product.name}</td>
              <td>{product.price}</td>
              <td>{product.quantity}</td>
              <td>{product.created_at}</td>
              <td>
                <Button
                  onClick={() => handleView(product.id)}
                  title="Visualizar"
                  color="#007BFF"
                />
                <Button
                  onClick={() => handleDelete(product.id)}
                  title="Deletar"
                  color="#DC3545"
                />
                <Button
                  onClick={() => handleUpdate(product.id)}
                  title="Atualizar"
                  color="#4CAF50"
                />
                {/*                <Button
                  onClick={() => handleUpdate(product.id)}
                  title="Histórico de Venda"
                  color="#FFA500"
          />*/}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ProductsDashboard;
