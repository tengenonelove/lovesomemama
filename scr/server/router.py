from src.server.routers import cars, masters, posts, repair_shops, staff, type_of_services, users


routers = (cars.router, masters.router, posts.router,
           repair_shops.router, staff.router,
           type_of_services.router, users.router)
