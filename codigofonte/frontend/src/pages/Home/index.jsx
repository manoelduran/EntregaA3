import Button from "../../components/Button";
import { useNavigate } from "react-router-dom";
import "./styles.css";
function Home() {
  const navigate = useNavigate();
  return (
    <div className="home-container">
      <h1>Lack of Creativity Store</h1>
      <div className="dashboard-buttons">
        <Button
          onClick={() => navigate("/customers")}
          title="Clientes"
          color="#800080"
        />
        <Button
          onClick={() => navigate("/products")}
          title="Produtos"
          color="#FF69B4"
        />
        <Button
          onClick={() => navigate("/orders")}
          title="Pedidos"
          color="#000000"
        />
      </div>
    </div>
  );
}

export default Home;
