import React, { useState, useEffect, useMemo } from "react";
import Button from "../../components/Button";
import "./styles.css";
import { api } from "../../services/api";
import { useNavigate } from "react-router-dom";

const ProductsLowStock = () => {
  const navigate = useNavigate();
  const [products, setProducts] = useState([]);

  useEffect(() => {
    api
      .get("/products")
      .then((response) => setProducts(response.data))
      .catch((error) => console.error("Erro ao buscar produtos:", error));
  }, []);
  const productsWithLowStock = useMemo(() => {
    const filteredProducts = products.filter(
      (product) => product.quantity < 10
    );
    const sortedProducts = filteredProducts.sort(
      (a, b) => a.quantity - b.quantity
    );
    return sortedProducts;
  }, [products]);

  console.log("productsWithLowStock", productsWithLowStock);
  return (
    <div className="table-container">
      <div className="table-header">
        <h2 className="table-title">Produtos Com Baixo Estoque</h2>
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
          {productsWithLowStock.map((product) => (
            <tr key={product.id}>
              <td>{product.id}</td>
              <td>{product.name}</td>
              <td>R$ {product.price}</td>
              <td>{product.quantity}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ProductsLowStock;
