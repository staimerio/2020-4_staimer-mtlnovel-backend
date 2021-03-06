# Retic
from retic import Router

# Controllers
import controllers.mtlnovel as mtlnovel

router = Router()

router.get("/novels", mtlnovel.get_all_search)

router.get("/novels/latest", mtlnovel.get_latest)

router \
    .get("/novels/chapters", mtlnovel.get_chapters_by_slug) \
    .post("/novels/chapters", mtlnovel.get_chapters_by_slug)