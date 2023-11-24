import React, { useState, useEffect } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { api } from '../../services/api';
import Button from '../../components/Button';
import './styles.css';

const CreateOrUpdateProduct = () => {
    const { state } = useLocation();
    const navigate = useNavigate();
    const productId = state && state.productId;

    const [product, setProduct] = useState({
        name: '',
        price: 0,
        quantity: 0,
    });
    const [error, setError] = useState('')
    const [loading, setLoading] = useState(false)
    useEffect(() => {
        if (!!productId) {
            setLoading(true)
            api.get(`/products/${productId}`)
                .then(response => {
                    setProduct(response.data)
                    setLoading(false)
                })
                .catch(error => console.error('Erro ao buscar produtos:', error));
        }
    }, []);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setProduct((prevProduct) => ({
            ...prevProduct,
            [name]: value,
        }));
    };

    const handleSubmit = async (e) => {
        try {
            e.preventDefault();
            if (productId) {
                const formData = new FormData(e.target);
                const productData = {};

                formData.forEach((value, key) => {
                    productData[key] = value;
                });
                await api.put(`/products/${productId}`, productData)
                navigate('/products');
            } else {
                const formData = new FormData(e.target);
                const productData = {};

                formData.forEach((value, key) => {
                    productData[key] = value;
                });
                await api.post('/products', productData)
                navigate('/products');
            }
        } catch (error) {
            setError(error.response.data.detail)
        }
    };
    if (loading) {
        return <div style={{ width: '100%', height: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>Carregando...</div>
    }
    if (error) {
        return (
            <>
                <div className='title-container'>
                    <h1>{productId ? 'Atualizar Produto' : 'Criar Produto'}</h1>
                    <Button title='Voltar' onClick={() => navigate(-1)} />
                </div>
                <div style={{ width: '100%', height: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>Error: {error}</div>
            </>
        )
    }
    return (
        <div className="container">
            <div className='title-container'>
                <h1>{productId ? 'Atualizar Produto' : 'Criar Produto'}</h1>
                <Button title='Voltar' onClick={() => navigate(-1)} />
            </div>

            <form onSubmit={handleSubmit}>
                <label>
                    Nome:
                    <input type="text" name="name" value={product.name} onChange={handleChange} />
                </label>


                <label>
                    Preço:
                    <input type="number" name="price" value={product.price} onChange={handleChange} />
                </label>
                <label>
                    Quantidade:
                    <input type="number" name="quantity" value={product.quantity} onChange={handleChange} />
                </label>

                <Button title={productId ? 'Atualizar' : 'Criar'} type="submit" />
            </form>
        </div>
    );
};

export default CreateOrUpdateProduct;