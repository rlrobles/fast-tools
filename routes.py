import constants as const
import render as ren


#TEMPLATE_RENDER_CONTROLLER = "generate-controller"
#TEMPLATE_RENDER_SERVERLESS = "generate-serverless"
#TEMPLATE_RENDER_CLASS = "generate-class"
#TEMPLATE_RENDER_REQUEST = "generate-request"

ROUTE_CONTROLLER = ren.generatePath(const.BASE_PATH,const.PATH_RENDER,const.TEMPLATE_RENDER_CONTROLLER)
ROUTE_SERVERLESS = ren.generatePath(const.BASE_PATH,const.PATH_RENDER,const.TEMPLATE_RENDER_SERVERLESS)
ROUTE_CLASS = ren.generatePath(const.BASE_PATH,const.PATH_RENDER,const.TEMPLATE_RENDER_CLASS)
ROUTE_REQUEST = ren.generatePath(const.BASE_PATH,const.PATH_RENDER,const.TEMPLATE_RENDER_REQUEST)
ROUTE_TEMPLATES = ren.generatePath(const.BASE_PATH,const.PATH_RENDER,const.TEMPLATE_TEMPLATES)