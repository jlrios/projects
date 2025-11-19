using Godot;
using System;

public partial class Character : CharacterBody2D
{
	[Export] public int Health { get; set; }
	[Export] public int Damage { get; set; }
	[Export] public float Speed { get; set; }

	public override void _Process(double delta)
	{
		Vector2 direction = Input.GetVector("ui_left", "ui_right", "ui_up", "ui_down");
		Velocity = direction * Speed;
		MoveAndSlide();
	}
}
