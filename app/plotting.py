import scanpy as sc


def umap_figure(adata):
    sc.tl.umap(adata)
    coords = adata.obsm["X_umap"]
    return {
        "x": coords[:, 0].tolist(),
        "y": coords[:, 1].tolist(),
        "clusters": adata.obs["leiden"].astype(str).tolist()
        if "leiden" in adata.obs
        else ["0"] * adata.n_obs,
    }
