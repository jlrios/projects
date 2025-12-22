import { Router } from 'express';

class AssetsRoutes {
    public router: Router = Router();

    constructor() {
        this.config();
    }

    config(): void {
        this.router.get('/', (req, res) => {
            res.send('Lista de equipos');
        });
    }
}

const assetsRoutes = new AssetsRoutes();

export default assetsRoutes.router;