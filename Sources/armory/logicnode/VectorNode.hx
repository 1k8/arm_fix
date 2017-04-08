package armory.logicnode;

import armory.math.Vec4;

class VectorNode extends LogicNode {

	var value = new Vec4();

	public function new(tree:LogicTree, x:Null<Float> = null, y:Null<Float> = null, z:Null<Float> = null) {
		super(tree);

		if (x != null) {
			addInput(new FloatNode(tree, x), 0);
			addInput(new FloatNode(tree, y), 0);
			addInput(new FloatNode(tree, z), 0);
		}
	}

	override function get(from:Int):Dynamic {
		value.x = inputs[0].get();
		value.y = inputs[1].get();
		value.z = inputs[2].get();
		return value;
	}

	override function set(value:Dynamic) {
		this.value = value;
	}
}
