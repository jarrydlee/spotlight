"""
Implementation of widget models and interfaces for widget creation.
"""

from typing import List, Optional

from pydantic import BaseModel, Extra, Field  # pylint: disable=no-name-in-module
from typing_extensions import Literal

from .lenses import Lens


class WidgetConfig(BaseModel, allow_population_by_field_name=True):
    # pylint: disable=too-few-public-methods
    """
    Base Spotlight widget configuration model.
    """


class Widget(BaseModel, extra=Extra.forbid):
    """
    Spotlight widget model.
    """

    # pylint: disable=too-few-public-methods
    type: str
    name: Optional[str] = None
    config: Optional[WidgetConfig] = None
    kind: Literal["widget"] = "widget"


class HistogramConfig(WidgetConfig):
    """
    Histogram configuration model.
    """

    # pylint: disable=too-few-public-methods
    column: Optional[str] = Field(None, alias="columnKey")
    stack_by_column: Optional[str] = Field(None, alias="stackByColumnKey")
    filter: bool = Field(False, alias="filter")


class Histogram(Widget):
    """
    Spotlight histogram model.
    """

    # pylint: disable=too-few-public-methods
    type: Literal["histogram"] = "histogram"
    config: Optional[HistogramConfig] = None


class ScatterplotConfig(WidgetConfig):
    """
    Scatter plot configuration model.
    """

    # pylint: disable=too-few-public-methods
    x_column: Optional[str] = Field(None, alias="xAxisColumn")
    y_column: Optional[str] = Field(None, alias="yAxisColumn")
    color_by_column: Optional[str] = Field(None, alias="colorBy")
    size_by_column: Optional[str] = Field(None, alias="sizeBy")
    filter: bool = Field(False, alias="filter")


class Scatterplot(Widget):
    """
    Spotlight scatter plot model.
    """

    # pylint: disable=too-few-public-methods
    type: Literal["scatterplot"] = "scatterplot"
    config: Optional[ScatterplotConfig] = None


TableView = Literal["full", "filtered", "selected"]


class TableConfig(WidgetConfig):
    """
    Table configuration model.
    """

    # pylint: disable=too-few-public-methods
    active_view: TableView = Field("full", alias="tableView")
    visible_columns: Optional[List[str]] = Field(None, alias="visibleColumns")
    sort_by_columns: Optional[List[List[str]]] = Field(None, alias="sorting")
    order_by_relevance: bool = Field(False, alias="orderByRelevance")


class Table(Widget):
    """
    Spotlight table model.
    """

    # pylint: disable=too-few-public-methods
    type: Literal["table"] = "table"
    config: Optional[TableConfig] = None


ReductionMethod = Literal["umap", "pca"]
UmapMetric = Literal[
    "euclidean", "standardized euclidean", "robust euclidean", "cosine", "mahalanobis"
]
PCANormalization = Literal["none", "standardize", "robust standardize"]


class SimilaritymapConfig(WidgetConfig):
    """
    Similarity map configuration model.
    """

    # pylint: disable=too-few-public-methods
    columns: Optional[List[str]] = Field(None, alias="placeBy")
    reduction_method: Optional[ReductionMethod] = Field(None, alias="reductionMethod")
    color_by_column: Optional[str] = Field(None, alias="colorBy")
    size_by_column: Optional[str] = Field(None, alias="sizeBy")
    filter: bool = Field(False, alias="filter")
    umap_nn: Optional[int] = Field(None, alias="umapNNeighbors")
    umap_metric: Optional[UmapMetric] = Field(None, alias="umapMetric")
    umap_min_dist: Optional[float] = Field(None, alias="umapMinDist")
    pca_normalization: Optional[PCANormalization] = Field(
        None, alias="pcaNormalization"
    )
    umap_balance: Optional[float] = Field(None, alias="umapMenuLocalGlobalBalance")
    umap_is_advanced: bool = Field(False, alias="umapMenuIsAdvanced")


class Similaritymap(Widget):
    """
    Spotlight similarity map model.
    """

    # pylint: disable=too-few-public-methods
    type: Literal["similaritymap"] = "similaritymap"
    config: Optional[SimilaritymapConfig] = None


NumInspectorColumns = Literal[1, 2, 4, 6, 8]


class InspectorConfig(WidgetConfig):
    """
    Inspector configuration model.
    """

    # pylint: disable=too-few-public-methods
    lenses: Optional[List[Lens]] = Field(default_factory=None, alias="views")
    num_columns: NumInspectorColumns = Field(4, alias="visibleColumns")


class Inspector(Widget):
    """
    Spotlight inspector model.
    """

    # pylint: disable=too-few-public-methods
    type: Literal["inspector"] = "inspector"
    config: Optional[InspectorConfig] = None


class Issues(Widget):
    """
    Spotlight issues widget
    """

    # pylint: disable=too-few-public-methods
    type: Literal["IssuesWidget"] = "IssuesWidget"
