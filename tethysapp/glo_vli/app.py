from tethys_sdk.base import TethysAppBase, url_map_maker
from tethys_sdk.app_settings import PersistentStoreDatabaseSetting

class GloVli(TethysAppBase):
    """
    Tethys app class for Vulnerability of Life and Infrastructure.
    """

    name = 'Vulnerability of Life and Infrastructure'
    index = 'glo_vli:home'
    icon = 'glo_vli/images/logo.jpg'
    package = 'glo_vli'
    root_url = 'glo-vli'
    color = '#16a085'
    description = 'Vulnerability of Life and Infrastructure'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='glo-vli',
                controller='glo_vli.controllers.home'
            ),
            UrlMap(
                name='add-point',
                url='glo-vli/add-point',
                controller='glo_vli.controllers.add_point'
            ),
            UrlMap(
                name='add-point-ajax',
                url='glo-vli/add-point/submit',
                controller='glo_vli.controllers_ajax.point_add'
            ),
            UrlMap(
                name='approve-points',
                url='glo-vli/approve-points',
                controller='glo_vli.controllers.approve_points'
            ),
            UrlMap(
                name='approve-points-table',
                url='glo-vli/approve-points/table',
                controller='glo_vli.controllers.approve_points_table'),
            UrlMap(
                name='update-points-ajax',
                url='glo-vli/approve-points/submit',
                controller='glo_vli.controllers_ajax.point_update'),
            UrlMap(
                name='delete-points-ajax',
                url='glo-vli/approve-points/delete',
                controller='glo_vli.controllers_ajax.point_delete'),
            UrlMap(
                name='add-polygon',
                url='glo-vli/add-polygon',
                controller='glo_vli.controllers.add_polygon'
            ),
            UrlMap(
                name='add-polygon-ajax',
                url='glo-vli/add-polygon/submit',
                controller='glo_vli.controllers_ajax.polygon_add'
            ),
            UrlMap(
                name='approve-polygons',
                url='glo-vli/approve-polygons',
                controller='glo_vli.controllers.approve_polygons'
            ),
            UrlMap(
                name='approve-polygons-table',
                url='glo-vli/approve-polygons/table',
                controller='glo_vli.controllers.approve_polygons_table'),
            UrlMap(
                name='update-polygons-ajax',
                url='glo-vli/approve-polygons/submit',
                controller='glo_vli.controllers_ajax.polygon_update'),
            UrlMap(
                name='delete-polygons-ajax',
                url='glo-vli/approve-polygons/delete',
                controller='glo_vli.controllers_ajax.polygon_delete'),
        )

        return url_maps

    def persistent_store_settings(self):
        """
        Define Persistent Store Settings.
        """
        ps_settings = (
            PersistentStoreDatabaseSetting(
                name='layers',
                description='layers database',
                initializer='glo_vli.model.init_layer_db',
                required=True,
                spatial=True
            ),
        )

        return ps_settings