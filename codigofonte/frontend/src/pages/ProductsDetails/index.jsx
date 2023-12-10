import React, { useEffect, useState } from 'react';
import './styles.css';
import { useLocation, useNavigate } from 'react-router-dom';
import { api } from '../../services/api';
import Button from '../../components/Button';

const ProductsDetails = () => {
    const { state } = useLocation();
    const navigate = useNavigate();
    const productId = state && state.productId;
    const [product, setProduct] = useState(undefined)
    useEffect(() => {
        api.get(`/products/${productId}`)
            .then(response => {
                setProduct(response.data)
            })
            .catch(error => console.error('Erro ao buscar clientes:', error));
    }, [])
    return (
        <div className="container">
            {Boolean(product) ? (<>
                <div className='title-container'>
                    <h1>Detalhes do Produto</h1>
                    <Button title='Voltar' onClick={() => navigate(-1)} />
                </div>
                <div className="customer-details">
                    <p><strong>Nome:</strong> {product.name}</p>
                    <p><strong>Preço:</strong> {product.price}</p>
                    <p><strong>Quantidade:</strong> {product.quantity}</p>
                    <p><strong>Criado em:</strong> {product.created_at}</p>
                </div>
            </>) : <div style={{ width: '100%', height: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>Carregando...</div>}
        </div>
    );
};

export default ProductsDetails;