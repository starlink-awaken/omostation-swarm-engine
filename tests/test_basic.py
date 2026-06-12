"""swarm_engine 基础测试"""

from swarm_engine import __init__
from swarm_engine.core import dag
from swarm_engine.core import router


class TestSwarmEngineInit:
    """Swarm Engine 初始化测试"""
    
    def test_import(self):
        """测试导入"""
        assert __init__ is not None


class TestDAG:
    """DAG 测试"""
    
    def test_import(self):
        """测试导入"""
        assert dag is not None


class TestRouter:
    """Router 测试"""
    
    def test_import(self):
        """测试导入"""
        assert router is not None
